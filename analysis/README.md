# Final 2026 analysis audit

This directory documents the audit layer used for the final 12-model study.

The public six-notebook workflow predates the final publication-grade experiment. The final experiment uses a fixed APTOS split, two architectures (ResNet-18 and EfficientNet-B0), RAW/CLEAN training, and seeds 13/42/77. The complete reviewer-defense script and saved prediction arrays are distributed in the manuscript reproducibility archive because the prediction/counterfactual files are large.

## `audit_predictions.py`

The audit script expects to be placed beside the final archive folders:

```text
predictions/
tables/
metadata/
```

It performs two checks without model retraining or model inference:

1. Recomputes ROC-AUC, average precision and Brier score from saved APTOS/Messidor logits and verifies common-raw counterfactual sensitivity means.
2. Recomputes the architecture-level external CLEAN-minus-RAW AUC interval using one class-stratified Messidor image resample shared by all three matched seed pairs, followed by paired seed resampling (10,000 replicates).

The shared-image procedure preserves the fact that all six models within an architecture were evaluated on the same external cohort. It remains image-conditional: the available evaluation metadata do not provide a verified paired-eye/patient grouping.

## Scientific interpretation

The final analysis does not treat reduced background sensitivity as proof of improved generalization. On identical raw APTOS inputs, CLEAN training substantially reduces EfficientNet-B0 response to the selected background interventions, but EfficientNet external discrimination decreases. ResNet-18 starts with much lower measured background sensitivity and shows no consistent external improvement.

The final APTOS split also contains cross-split exact and near-duplicate structure. The manuscript therefore does not claim patient-independent internal validation; sensitivity analyses exclude suspicious development-test neighbors to determine whether the principal internal findings are explained solely by those detected redundancies.

See the repository-level `REPRODUCIBILITY.md` for the complete protocol and limitations.
