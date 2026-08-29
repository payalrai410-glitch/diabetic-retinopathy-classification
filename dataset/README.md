# 🩺 Diabetic Retinopathy Classification

A deep learning project for classifying diabetic retinopathy
from colored fundus retina images.

## 📌 Project Overview

Diabetic retinopathy is an eye disease associated with diabetes.
This project prepares a fundus image dataset for machine learning
classification.

## 🗂️ Classes

The dataset contains four classes:

| Class | Description |
|---|---|
| No_DR | No diabetic retinopathy |
| Mild | Mild diabetic retinopathy |
| Moderate | Moderate diabetic retinopathy |
| Severe | Severe diabetic retinopathy |

## 🔧 Preprocessing

The images were prepared using Python and Google Colab.

- Image resizing: 224 × 224
- Train/Test split: 80/20
- Normalization: 0–1
- Four-class classification

## 📊 Dataset

Dataset source:

https://www.kaggle.com/datasets/sovitrath/diabetic-retinopathy-2015-data-colored-resized

The complete dataset is approximately 2.0 GB and contains
34,418 processed images.

The full image dataset is not included in this GitHub repository
because of its large size.

## 📓 Notebook

The complete preprocessing workflow is available here:

`notebooks/diabetic_retinopathy.ipynb`

## 📁 Repository Structure

```text
diabetic-retinopathy-classification/
│
├── README.md
├── notebooks/
│   └── diabetic_retinopathy.ipynb
├── preprocessing/
│   └── preprocessing.py
├── dataset/
│   └── README.md
└── results/
    └── sample_predictions/
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPOSITORY/blob/main/preprocessing.ipynb)
