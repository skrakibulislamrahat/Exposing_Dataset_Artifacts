# Reduced background sensitivity does not ensure external discrimination in fundus classifiers

This repository contains the public research code and documentation for a diabetic-retinopathy (DR) fundus-image study of background shortcut sensitivity, artifact-aware border cropping, and cross-dataset generalization.

The final study asks a specific question: **if a preprocessing/training regime makes a classifier less responsive to selected non-retinal background interventions, does external discrimination improve?** The answer in these experiments is no. The relationship is architecture-dependent.

## Final experimental design

- Development dataset: APTOS 2019, binary endpoint grade 0 vs grade >0.
- Fixed stratified image split: 2,563 train / 549 validation / 550 test (split seed 2026).
- Architectures: ResNet-18 and EfficientNet-B0.
- Training regimes: original framing (RAW) and intensity-based border-cropped framing (CLEAN).
- Training seeds: 13, 42, 77.
- Total trained variants: 12.
- External evaluation: 1,744 gradable images from the project's existing processed Messidor-2 archive.
- Messidor-2 was not used for training, early stopping, checkpoint selection, calibration fitting, or threshold selection.

The main robustness comparison evaluates RAW- and CLEAN-trained models on **identical raw APTOS inputs**. Background interventions include gray replacement, background noise, and peripheral-ring perturbations at multiple severities. The final audit also includes validation-only temperature scaling and threshold selection, background-only label probes, source classification, quantitative Grad-CAM, and exact/perceptual/embedding-based duplicate checks.

## Main findings

Across the 12 variants, APTOS test ROC-AUC was approximately 0.9963-0.9992, whereas external Messidor-2 ROC-AUC was approximately 0.5643-0.6642.

On identical raw APTOS inputs, CLEAN training reduced EfficientNet-B0's mean strongest-level background sensitivity by about 49%, while ResNet-18 started substantially lower and changed only modestly and inconsistently. A similar EfficientNet reduction appeared on the common Messidor representation. Despite that reduction, EfficientNet-B0 external ROC-AUC decreased under CLEAN training. ResNet-18 showed no consistent architecture-level external improvement.

The audit also found strong label-associated information outside the estimated retinal field, complete separability between the available APTOS and processed Messidor representations using both low-level and frozen-image features, and cross-split duplicate/near-duplicate structure in APTOS. Near-duplicate exclusion analyses did not explain away the near-ceiling internal AUC or the background-only label signal. These results do **not** establish patient-independent internal validation because patient identifiers were unavailable.

The study therefore does not claim that cropping improves external generalization. Its main conclusion is narrower: **reducing measured background nuisance sensitivity is not sufficient evidence of improved cross-domain discrimination.**

## Repository structure

```text
.
├── analysis/
│   ├── README.md
│   └── audit_predictions.py
├── notebooks/
│   ├── 01_dataset_inspection.ipynb
│   ├── 02_border_artifact_classifier.ipynb
│   ├── 03_train_model_with_artifacts.ipynb
│   ├── 04_preprocess_and_clean_images.ipynb
│   ├── 05_train_model_without_artifacts.ipynb
│   └── 06_external_validation_messidor2.ipynb
├── DATA_AVAILABILITY.md
├── REPRODUCIBILITY.md
├── requirements.txt
└── CITATION.cff
```

The numbered notebooks document the historical workflow that led to the project. The `analysis/` directory documents the final reviewer-defense/audit stage. Large checkpoints, prediction arrays, evaluation caches, and raw datasets are not stored in GitHub.

## Important reproducibility boundary

The exact external evaluation in the final study used the project's already processed `Messidor_2/my_preprocessed` archive. It should not be described as evaluation on untouched raw Messidor-2 images, and the study did not perform a raw-vs-cropped factorial experiment on Messidor-2.

The final submission/reproducibility archive contains the complete reviewer-defense script, final publication-upgrade notebook, saved prediction arrays, analysis tables, metadata, hashes, and figure-generation code. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the relationship between the public repository and that archive.

## Data

- **APTOS 2019 Blindness Detection** — development dataset.
- **Messidor-2** — external retinal dataset; the final experiment used the project's existing processed representation.

Dataset images are not redistributed here. Users must obtain data from the official providers and follow their licenses and terms. See [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md).

## Responsible use

This repository is research code. It is **not a clinical diagnostic system** and the reported experiments do not establish a clinically validated operating point or prospective patient-level performance.

## Citation

Publication metadata will be added after the associated manuscript has a stable bibliographic record. Until then, cite the repository URL and access date when using this code directly.
