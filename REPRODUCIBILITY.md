# How to reproduce the project

There are two parts to this repository:

1. The six notebooks show the original development workflow.
2. The later analysis added a second architecture, three training seeds, calibration, background tests, duplicate checks, and statistical analysis.

The notebooks are useful for following the project from the beginning, but they do not reproduce every number from the final 12-model study by themselves.

## What is available here

- Six notebooks for data inspection, source classification, raw-image training, border cropping, cleaned-image training, and external testing.
- `analysis/audit_predictions.py`, which recalculates metrics from saved predictions and repeats the paired external bootstrap analysis.
- `analysis/README.md`, which explains the files expected by the audit script.
- The package list in `requirements.txt`.

The final archive also contains model checkpoints, saved predictions, counterfactual outputs, result tables, metadata, hashes, and the final experiment notebook. Those larger generated files are not stored in this GitHub repository.

## Notebook order

Run the notebooks in this order to follow the original workflow:

1. `01_dataset_inspection.ipynb`
2. `02_border_artifact_classifier.ipynb`
3. `03_train_model_with_artifacts.ipynb`
4. `04_preprocess_and_clean_images.ipynb`
5. `05_train_model_without_artifacts.ipynb`
6. `06_external_validation_messidor2.ipynb`

The paths near the beginning of each notebook may need to be changed for a local or Google Drive setup.

## Data paths used in Colab

The completed project used this folder layout:

```text
/content/drive/MyDrive/Fundus_Artifact_Project
/content/drive/MyDrive/Datasets/APTOS_2019/train_images
/content/drive/MyDrive/Datasets/APTOS_2019/train.csv
/content/drive/MyDrive/Fundus_Artifact_Project/Messidor_2/my_preprocessed
/content/drive/MyDrive/Fundus_Artifact_Project/Messidor_2/grades.csv
```

The Messidor-2 detail matters. The final external test used the already processed `my_preprocessed` images. It did not compare raw and cleaned Messidor-2 images. Using raw Messidor-2 files would not reproduce the same external experiment.

## Final training settings

- Image size: 224 x 224
- Batch size: 32
- Maximum epochs: 12
- Early-stopping patience: 3
- Optimizer: AdamW
- Learning rate: 1e-4
- Weight decay: 1e-4
- Loss: `BCEWithLogitsLoss` with positive-class weighting calculated from the training split
- Starting weights: torchvision ImageNet weights
- Augmentation: horizontal flip with probability 0.5, vertical flip with probability 0.5, and rotation up to 10 degrees
- Checkpoint selection: highest APTOS validation ROC-AUC
- Calibration: one temperature value fitted only on APTOS validation logits
- Threshold: selected for balanced accuracy on APTOS validation data and then kept fixed

The final experiment used ResNet-18 and EfficientNet-B0, RAW and CLEAN training, and seeds 13, 42, and 77. The fixed APTOS split contained 2,563 training, 549 validation, and 550 test images.

## Prediction audit

The audit script recalculates ROC-AUC, average precision, and Brier score from saved logits. It also checks the background-sensitivity summaries and repeats the external CLEAN-minus-RAW bootstrap comparison.

All models within one architecture were tested on the same Messidor-2 images. The bootstrap therefore uses the same class-stratified image resample for the matched RAW and CLEAN models, followed by paired resampling across the three seeds.

This analysis still has limits. Only three seeds were used. Verified patient or paired-eye identifiers were not available for the external data, and APTOS did not include patient identifiers for a patient-independent split.

## Environment

Install the packages listed in `requirements.txt`. A GPU is recommended for model training and inference. The saved-prediction audit can run on a CPU.

The final archive includes `environment_and_hashes.json`, which records the completed run's environment and checkpoint hashes.

## What cannot be reproduced from GitHub alone

- The raw datasets are not included.
- Large model checkpoints and saved prediction arrays are not included.
- Exact reproduction of the external pixels requires the same processed Messidor-2 archive.
- Small differences can occur during retraining because of framework and GPU nondeterminism.

For a new run, record the dataset release, split file or hash, package versions, hardware, random seeds, preprocessing path, selected checkpoints, external image representation, and any change from the settings above.
