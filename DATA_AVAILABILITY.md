# Data availability

The retinal images are not included in this repository.

The project uses APTOS 2019 for training, validation, and internal testing. It uses 1,744 gradable images from the project's processed Messidor-2 archive for external testing. The original datasets must be obtained from their providers and used under their own licenses and access rules.

The exact external test used `Messidor_2/my_preprocessed`. Using raw Messidor-2 images instead would change the input data and would not reproduce the reported experiment.

The final project archive contains saved predictions, row-order metadata, result tables, hashes, and analysis code. Raw retinal images and model checkpoint files are not distributed through GitHub.

Do not commit dataset archives, credentials, personal information, or patient-linked files to this repository.
