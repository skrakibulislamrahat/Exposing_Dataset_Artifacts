# Exposing Dataset Artifacts in Medical AI

## When fundus-image models learn acquisition artifacts instead of disease

This repository contains the reproducibility code for a research study on **dataset artifacts and shortcut learning in diabetic-retinopathy (DR) classification**. The central question is whether a retinal classifier can achieve apparently strong performance while relying on non-clinical image cues such as borders, padding, or acquisition-specific appearance.

The project compares models trained on original fundus images with models trained after artifact-aware preprocessing, and then evaluates generalization on an external retinal dataset.

## Research questions

1. Can a CNN explicitly detect border/acquisition artifacts in fundus images?
2. Do DR classifiers trained on unprocessed images attend to those artifacts?
3. Does artifact-aware preprocessing change model attention and predictive behavior?
4. Does the resulting model generalize more reliably to an external dataset?

## Experimental pipeline

| Stage | Notebook | Purpose |
|---|---|---|
| 1 | `notebooks/01_dataset_inspection.ipynb` | Inspect APTOS 2019 and Messidor-2 metadata/images and audit dataset availability. |
| 2 | `notebooks/02_border_artifact_classifier.ipynb` | Train a ResNet-based classifier to detect border artifacts and inspect attention with Grad-CAM. |
| 3 | `notebooks/03_train_model_with_artifacts.ipynb` | Train the baseline DR classifier on images that retain acquisition artifacts. |
| 4 | `notebooks/04_preprocess_and_clean_images.ipynb` | Apply artifact-aware preprocessing to produce cleaned fundus images. |
| 5 | `notebooks/05_train_model_without_artifacts.ipynb` | Train the DR classifier on preprocessed images and generate interpretability outputs. |
| 6 | `notebooks/06_external_validation_messidor2.ipynb` | Evaluate the trained model on Messidor-2 using accuracy, ROC-AUC, ROC curves, and confusion matrices. |

The manuscript-assembly notebook is intentionally **not** included. This repository is for research code and reproducibility, not for distributing unpublished manuscript drafts.

## Datasets

The experiments use two public retinal-imaging resources:

- **APTOS 2019 Blindness Detection** — primary development dataset.
- **Messidor-2** — external validation dataset.

Dataset files are not redistributed here. Users are responsible for obtaining the datasets from their official sources and complying with their licenses and terms. See [`DATA_AVAILABILITY.md`](DATA_AVAILABILITY.md).

## Methods represented in the code

The notebooks use Python with PyTorch/torchvision, OpenCV, pandas, NumPy, scikit-learn, Matplotlib, Seaborn, Pillow, TorchCAM, and `pytorch-grad-cam`. The experimental code includes ResNet-based classification, artifact-aware image preprocessing, Grad-CAM-style interpretability, and external-validation metrics.

## Reproducibility

The original experiments were developed in Google Colab and use paths under:

```text
/content/drive/MyDrive/Fundus_Artifact_Project
```

Update the path configuration for your environment before execution. The public notebooks have had stored outputs and volatile Colab execution metadata removed so the repository reflects the executable analysis rather than cached results.

For the recommended execution order and environment notes, see [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

## Repository structure

```text
.
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
└── README.md
```

## Research status

This repository documents an active research line. Publication metadata and a formal citation will be added when a stable archival version is available. Until then, cite the repository URL and access date if you build directly on this code.

## Responsible use

This code is provided for research and reproducibility. It is **not a clinical diagnostic system** and should not be used for patient-care decisions without appropriate validation, governance, and regulatory review.
