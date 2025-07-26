# Exposing Dataset Artifacts in Medical AI: When Fundus Models Learn Borders Instead of Disease

This repository contains all source code, saved outputs, and visualizations for the research project:

**“Exposing Dataset Artifacts in Medical AI: When Fundus Models Learn Borders Instead of Disease”**  
🔬 Submitted to a Q1 journal (e.g., *npj Digital Medicine*, *Artificial Intelligence in Medicine*, *IEEE J-BHI*)

## 🔍 Summary

This study investigates how public deep learning models for diabetic retinopathy (DR) often overfit to visual artifacts—like black image borders, scanner text, or padding—rather than clinical pathology. We:
- Train a CNN to detect image borders (binary border classifier)
- Train a DR model on raw vs. preprocessed (artifact-free) fundus images
- Use Grad-CAM visualizations to verify attention shift from artifacts to lesions
- Evaluate generalization using Messidor-2

## 📁 Folder Structure

Fundus_Artifact_Project/
├── APTOS_2019/                    → Original APTOS dataset
│   ├── train_images/             → Raw fundus images
│   └── train.csv                 → DR labels
│
├── Messidor_2/                   → Messidor-2 dataset for external validation
│   └── dataset.zip              → Original compressed files
│
├── Binary_Border_Classifier/     → Data and models for border classifier
├── Raw_DR_Classifier/            → Data and models for raw (unprocessed) DR classifier
│
├── Results/                      → All model outputs, logs, and visualizations
│   ├── border_artifact_model/  → Border classifier results
│   ├── raw_image_model/        → Raw DR model results
│   ├── dr_artifact_model/      → Clean DR model results (after preprocessing)
│   └── final_figures/          → Final visual figures used in the paper
│
├── Notebooks/                    → Complete training and evaluation notebooks
│   ├── 01_Dataset_Inspection.ipynb
│   ├── 02_Border_Classifier.ipynb
│   ├── 03_Raw_DR_Model.ipynb
│   ├── 04_Preprocessing.ipynb
│   ├── 05_Cleaned_DR_Model.ipynb
│   ├── 06_External_Validation.ipynb
│   └── 07_Paper_Figures_Assembly.ipynb



## 📊 Visualizations

All Grad-CAMs, ROC curves, and confusion matrices used in the paper are stored in:

## 🧠 Models Used
- **ResNet-18** (PyTorch)
- Training pipeline includes:
  - Data augmentation
  - Cross-entropy loss
  - Adam optimizer

## 📝 Citation (BibTeX — when published)
*To be updated after peer-reviewed publication.*

---

If you use this project or build on it, please consider citing and linking back.

---

