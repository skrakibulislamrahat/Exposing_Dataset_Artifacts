# Reproducibility Guide

## What is final vs historical

The six numbered notebooks in `notebooks/` document the original project development. They are retained for provenance, but they do **not** by themselves define the final 2026 12-model analysis.

The final manuscript uses a publication-upgrade workflow with:

- a fixed APTOS split (2,563 train / 549 validation / 550 test; split seed 2026),
- ResNet-18 and EfficientNet-B0,
- RAW and CLEAN training regimes,
- seeds 13, 42, 77,
- validation-only checkpoint/calibration/threshold choices,
- common-input counterfactual background tests,
- external evaluation on the project's existing processed Messidor-2 representation,
- duplicate/near-duplicate auditing,
- background-only and source-classification probes,
- quantitative Grad-CAM,
- paired and seed-aware bootstrap analyses.

The full final reviewer-defense script, publication-upgrade notebook, saved prediction arrays, metadata, analysis tables, environment record and hashes are distributed in the manuscript reproducibility archive rather than GitHub because several files are large.

## Public repository

The public repository contains:

1. Historical notebooks (`notebooks/01` through `06`).
2. `analysis/audit_predictions.py`, which independently recomputes saved prediction-level metrics and the shared-image/paired-seed external bootstrap when run against the final reproducibility archive.
3. `analysis/README.md`, which documents the expected final archive layout and audit checks.

## Historical notebook order

If reproducing the original development workflow, run:

1. `01_dataset_inspection.ipynb`
2. `02_border_artifact_classifier.ipynb`
3. `03_train_model_with_artifacts.ipynb`
4. `04_preprocess_and_clean_images.ipynb`
5. `05_train_model_without_artifacts.ipynb`
6. `06_external_validation_messidor2.ipynb`

Do not use those historical notebooks alone to reproduce the final manuscript numbers.

## Data layout used by the final project

The completed Colab project used paths equivalent to:

```text
/content/drive/MyDrive/Fundus_Artifact_Project
/content/drive/MyDrive/Datasets/APTOS_2019/train_images
/content/drive/MyDrive/Datasets/APTOS_2019/train.csv
/content/drive/MyDrive/Fundus_Artifact_Project/Messidor_2/my_preprocessed
/content/drive/MyDrive/Fundus_Artifact_Project/Messidor_2/grades.csv
```

The external representation is important: the final experiment used the existing processed Messidor archive. It was **not** a raw-vs-clean Messidor preprocessing experiment.

## Final training protocol

- Image size: 224 x 224.
- Batch size: 32.
- Maximum epochs: 12.
- Early-stopping patience: 3.
- Optimizer: AdamW.
- Learning rate: 1e-4.
- Weight decay: 1e-4.
- Loss: `BCEWithLogitsLoss` with training-split positive weighting.
- Initialization: torchvision ImageNet weights.
- Augmentation: horizontal flip (0.5), vertical flip (0.5), rotation +/-10 degrees.
- Model selection: best APTOS validation ROC-AUC.
- Calibration: scalar temperature fitted on APTOS validation logits only.
- Operating threshold: selected on APTOS validation for balanced accuracy and then frozen.

## Final analysis checks

The independent audit recomputes ROC-AUC, average precision and Brier score from saved logits and verifies common-raw sensitivity means from the saved counterfactual arrays. It also recomputes an architecture-level external CLEAN-minus-RAW AUC interval using one stratified Messidor image resample shared across the three matched seed pairs, followed by paired seed resampling.

The final manuscript reports the limitations of this image-conditional inference: only three seeds are available, paired-eye grouping for the evaluated external metadata is unavailable, and the APTOS split cannot be claimed patient independent because patient identifiers are absent.

## Environment

Install the packages in `requirements.txt`. GPU acceleration is needed for practical retraining and final model inference, but the independent saved-prediction audit is CPU-friendly.

The completed reviewer-defense run recorded the exact environment and checkpoint hashes in `environment_and_hashes.json` within the reproducibility archive.

## Reproducibility boundaries

- Raw datasets are not redistributed.
- Large checkpoints and saved prediction arrays are not stored in GitHub.
- Exact reproduction of the processed Messidor pixels requires the same project archive; substituting raw Messidor images changes the evaluated representation.
- APTOS metadata in the final split do not include patient identifiers.
- Cross-split exact/perceptual/embedding redundancy is explicitly audited rather than assumed absent.
- Framework/GPU nondeterminism can produce small run-to-run differences if models are retrained.

## Verification record

For an independent replication, record the dataset release, split file/hash, framework versions, hardware, all training seeds, preprocessing path, selected checkpoints, external representation, and any deviation from the final protocol above.
