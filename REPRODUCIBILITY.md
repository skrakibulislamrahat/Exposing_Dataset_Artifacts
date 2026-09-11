# Reproducibility Guide

## Recommended order

Run the notebooks in numerical order. The later notebooks expect artifacts produced by earlier stages.

1. `01_dataset_inspection.ipynb`
2. `02_border_artifact_classifier.ipynb`
3. `03_train_model_with_artifacts.ipynb`
4. `04_preprocess_and_clean_images.ipynb`
5. `05_train_model_without_artifacts.ipynb`
6. `06_external_validation_messidor2.ipynb`

## Environment

The original implementation was developed in Google Colab. Create an isolated Python environment and install the dependencies in `requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

GPU acceleration is recommended for model training but is not required for dataset inspection and most preprocessing steps.

## Data layout

The notebooks were originally written against the following Colab root:

```text
/content/drive/MyDrive/Fundus_Artifact_Project
```

Expected subdirectories include the APTOS dataset, Messidor-2, and experiment-output directories. If you run outside Colab, replace the root path with a local or mounted data directory.

## Reproducibility boundaries

- Raw datasets are excluded from version control.
- Model checkpoints and large generated artifacts are excluded from the public repository.
- Stored notebook outputs were removed before publication to reduce repository noise and prevent cached outputs from being mistaken for a fresh execution.
- Exact numerical reproduction may depend on framework versions, GPU kernels, random seeds, and the precise dataset release used.

## Verification

For a clean replication, record:

- Python and package versions;
- hardware/GPU model;
- dataset source and retrieval date;
- preprocessing settings;
- random seed(s);
- final metrics and confusion matrices;
- any deviations from the notebook configuration.
