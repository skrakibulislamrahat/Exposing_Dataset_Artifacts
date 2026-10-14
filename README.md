# Testing whether cleaner fundus images reduce shortcut learning

This project looks at a simple problem in diabetic retinopathy classification. A model may get a high score by learning from black borders, padding, or other dataset-specific patterns instead of using only retinal information.

I compared models trained on the original APTOS images with models trained after a simple border-cropping step. I then tested both versions on APTOS and on a separate processed Messidor-2 dataset. The main question was whether reducing sensitivity to the background would also improve performance on a different dataset.

In these experiments, it did not consistently improve external performance. The result also depended on the model architecture.

## Experiment setup

- **Main dataset:** APTOS 2019, converted to a binary task: grade 0 vs. grade greater than 0.
- **Fixed split:** 2,563 training, 549 validation, and 550 test images. The split seed was 2026.
- **Models:** ResNet-18 and EfficientNet-B0.
- **Image versions:** original framing (RAW) and border-cropped framing (CLEAN).
- **Training seeds:** 13, 42, and 77.
- **Total model runs:** 12.
- **External test set:** 1,744 gradable images from the processed Messidor-2 archive used in this project.

Messidor-2 was used only for external testing. It was not used for training, early stopping, checkpoint selection, calibration, or threshold selection.

For the main background test, RAW- and CLEAN-trained models were evaluated on the same raw APTOS images. I tested gray background replacement, background noise, and changes to the outer ring of the image. The final analysis also includes temperature scaling, validation-based threshold selection, background-only prediction tests, source classification, Grad-CAM, and duplicate checks.

## Main results

APTOS test ROC-AUC ranged from about 0.9963 to 0.9992. External Messidor-2 ROC-AUC was much lower, ranging from about 0.5643 to 0.6642.

For EfficientNet-B0, CLEAN training reduced the strongest measured background response by about 49% on identical raw APTOS inputs. However, its external ROC-AUC decreased. ResNet-18 started with lower background sensitivity and did not show a consistent external improvement after CLEAN training.

The analysis also found label-related information outside the estimated retinal area, clear differences between the available APTOS and processed Messidor images, and exact or near-duplicate images across APTOS splits. Removing suspicious near-duplicates did not remove the very high internal AUC or the background-only signal.

Patient identifiers were not available for APTOS, so the internal split cannot be described as patient independent. The conclusion is therefore limited: making a model less responsive to the tested background changes does not automatically make it generalize better to another dataset.

## Repository contents

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

The six notebooks show the earlier project workflow. The `analysis/` folder contains the independent prediction-level audit used for the final study. The final study added more models and checks than the original notebook sequence.

## Reproducibility note

The public repository does not include raw datasets, large checkpoints, or saved prediction arrays. The final analysis archive contains those generated files together with the final experiment notebook, tables, hashes, and environment record.

The external experiment used the project's existing processed `Messidor_2/my_preprocessed` images. It was not a comparison of raw and cleaned Messidor-2 images. Replacing that archive with raw Messidor-2 images would create a different experiment.

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the exact training settings, notebook order, expected data paths, and the limits of the public repository.

## Data

- [APTOS 2019 Blindness Detection](https://www.kaggle.com/c/aptos2019-blindness-detection) was used for training, validation, and internal testing.
- [Messidor-2](https://www.adcis.net/en/third-party/messidor2/) was used for external testing through the processed project archive described above.

The images are not redistributed. Anyone using the datasets must obtain them from the original providers and follow their terms. More details are in [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md).

## Responsible use

This code is for research and coursework. It is not a clinical diagnostic system, and the reported results do not establish a clinically validated operating point or prospective patient-level performance.

## Citation

The paper does not yet have stable publication information. Until it does, cite the repository URL and the date it was accessed.
