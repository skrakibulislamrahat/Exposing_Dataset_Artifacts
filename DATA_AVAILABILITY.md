# Data Availability

This repository does not redistribute retinal-image datasets.

The final study uses **APTOS 2019 Blindness Detection** for model development and an existing **processed Messidor-2 archive** for external evaluation. Obtain the underlying datasets from authorized sources and follow their licenses, access requirements, and terms of use.

Important reproducibility boundary: the final external experiment used the project-specific processed Messidor representation (`Messidor_2/my_preprocessed`). Substituting raw Messidor-2 images changes the evaluated input representation and does not reproduce the exact external experiment reported in the manuscript.

The manuscript reproducibility archive contains saved prediction arrays, row-order metadata, numerical analysis tables, hashes, and analysis code. Source images and model checkpoint binaries are not redistributed through GitHub.

Do not commit raw retinal images, dataset archives, credentials, personal data, or locally generated patient-linked files to this repository.
