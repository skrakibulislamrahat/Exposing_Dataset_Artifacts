from pathlib import Path
import numpy as np
import pandas as pd
from scipy.special import expit
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss

ROOT = Path(__file__).resolve().parent
P = ROOT / 'predictions'
T = ROOT / 'tables'
M = ROOT / 'metadata'
out = ROOT / 'independent_audit'
out.mkdir(exist_ok=True)

seeds = [13, 42, 77]
archs = ['resnet18', 'efficientnet_b0']
y = pd.read_csv(M / 'messidor_meta.csv').y.to_numpy()
metrics = pd.read_csv(T / 'final_model_metrics.csv')
checks = []

for arch in archs:
    for regime in ['raw', 'clean']:
        for seed in seeds:
            key = f'{arch}__{regime}__seed{seed}'
            z = np.load(P / f'{key}__eval_logits.npz')
            for ds, zk, mf in [
                ('APTOS_test_native', 'test_' + regime, 'aptos_test_meta.csv'),
                ('Messidor2', 'messidor', 'messidor_meta.csv'),
            ]:
                yy = pd.read_csv(M / mf).y.to_numpy()
                pp = expit(z[zk])
                row = metrics[(metrics.model == key) & (metrics.dataset == ds)].iloc[0]
                for metric, value in [
                    ('roc_auc', roc_auc_score(yy, pp)),
                    ('pr_auc', average_precision_score(yy, pp)),
                    ('brier', brier_score_loss(yy, pp)),
                ]:
                    checks.append(
                        dict(
                            model=key,
                            dataset=ds,
                            metric=metric,
                            recomputed=value,
                            saved=row[metric],
                            absolute_difference=abs(value - row[metric]),
                        )
                    )

            cf = np.load(P / f'{key}__commonraw_level4.npz')
            base = cf['base_raw']
            assert np.allclose(base, expit(z['test_raw']))
            ss = np.mean(
                [abs(cf[f + '_4'].astype(float) - base.astype(float)) for f in ['gray', 'noise', 'ring']],
                axis=0,
            )
            row = pd.read_csv(T / 'artifact_sensitivity_common_raw_model_level.csv').set_index('model').loc[key]
            assert abs(ss.mean() - row.mean_level4_artifact_sensitivity) < 1e-10

pd.DataFrame(checks).to_csv(out / 'prediction_metric_verification.csv', index=False)
assert max(x['absolute_difference'] for x in checks) < 1e-7

# Audit-only reanalysis of existing predictions; no model fitting or inference.
# One stratified image resample is shared by all seed pairs, preserving common-cohort dependence.
B = 10000
rng = np.random.default_rng(2026)
i0 = np.where(y == 0)[0]
i1 = np.where(y == 1)[0]

allp = {
    a: np.stack(
        [
            expit(np.load(P / f'{a}__{r}__seed{s}__eval_logits.npz')['messidor']).astype(float)
            for s in seeds
            for r in ['raw', 'clean']
        ]
    )
    for a in archs
}


def prep(p):
    order = np.argsort(p)
    sortedp = p[order]
    starts = np.r_[0, np.where(np.diff(sortedp) != 0)[0] + 1]
    return order, starts


prepared = {a: [prep(p) for p in ps] for a, ps in allp.items()}


def weighted_auc(w, order, starts):
    a = np.add.reduceat(w[order] * (y[order] == 1), starts)
    b = np.add.reduceat(w[order] * (y[order] == 0), starts)
    return np.sum(a * (np.cumsum(b) - 0.5 * b)) / (a.sum() * b.sum())


for a in archs:
    for p, (order, starts) in zip(allp[a], prepared[a]):
        assert abs(weighted_auc(np.ones(len(y)), order, starts) - roc_auc_score(y, p)) < 1e-12

vals = {a: [] for a in archs}
for _ in range(B):
    ix = np.r_[rng.choice(i0, len(i0)), rng.choice(i1, len(i1))]
    w = np.bincount(ix, minlength=len(y))
    sampled_seeds = rng.integers(0, 3, 3)
    for a in archs:
        aucs = np.array([weighted_auc(w, o, t) for o, t in prepared[a]]).reshape(3, 2)
        vals[a].append((aucs[:, 1] - aucs[:, 0])[sampled_seeds].mean())

rows = []
for a in archs:
    observed = np.array([roc_auc_score(y, p) for p in allp[a]]).reshape(3, 2)
    delta = (observed[:, 1] - observed[:, 0]).mean()
    lo, hi = np.percentile(vals[a], [2.5, 97.5])
    rows.append(
        dict(
            architecture=a,
            mean_seed_delta_auc=delta,
            ci_low=lo,
            ci_high=hi,
            replicates=B,
            method='shared stratified image resample and paired seed resample',
        )
    )

result = pd.DataFrame(rows)
result.to_csv(out / 'external_shared_image_bootstrap.csv', index=False)
print(result.to_string(index=False))
print('Verified 72 discrimination/probability metrics and 12 common-input sensitivity means.')
