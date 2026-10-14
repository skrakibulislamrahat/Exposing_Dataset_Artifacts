# Prediction audit

This folder contains the script used to check the saved predictions from the final 12-model experiment.

The original six notebooks were written earlier in the project. The final experiment used a fixed APTOS split, ResNet-18 and EfficientNet-B0, RAW and CLEAN training, and seeds 13, 42, and 77. The complete final archive is separate because the prediction and counterfactual files are too large for this repository.

## Files expected by `audit_predictions.py`

Place the script beside these folders from the final archive:

```text
predictions/
tables/
metadata/
```

The script performs two checks:

1. It recalculates ROC-AUC, average precision, and Brier score from saved APTOS and Messidor-2 logits. It also checks the saved background-sensitivity means.
2. It repeats the external CLEAN-minus-RAW AUC bootstrap using the same class-stratified Messidor-2 image resample for each matched seed pair, followed by paired resampling across the three seeds.

The models were tested on the same external images, so the paired procedure keeps that shared test set in the comparison. It is still an image-level analysis because verified patient or paired-eye identifiers were not available.

## How to read the result

CLEAN training made EfficientNet-B0 less responsive to the tested background changes, but its external discrimination decreased. ResNet-18 started with lower measured background sensitivity and did not show a consistent external improvement.

APTOS also contained exact and near-duplicate images across splits. The final analysis removes suspicious development-test neighbors as a sensitivity check. Patient identifiers were unavailable, so the internal results are not described as patient-independent validation.

See [../REPRODUCIBILITY.md](../REPRODUCIBILITY.md) for the full settings and limitations.
