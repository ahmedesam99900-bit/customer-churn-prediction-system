# Customer Churn Prediction System

## Project Overview

This project aims to build an end-to-end Machine Learning system that predicts whether a customer is likely to leave the company based on customer information and service usage.

---

## Business Problem

The company loses customers over time, which leads to a decrease in revenue. The goal of this project is to identify customers who are likely to leave the company before they actually do, allowing the business to take preventive actions.

---

## Business Value

Retaining existing customers is generally less costly than replacing them with new ones. By predicting potential churn, the company can improve customer retention, reduce revenue loss, and make better business decisions.

---

## Stakeholders

- Customer Retention Team
- Marketing Team
- Customer Success Team
- Business Management

---

## Target Variable

**Churn**

- Yes → The customer left the company.
- No → The customer stayed with the company.

---

## Problem Type

Binary Classification

The model predicts one of two possible classes:
- Churn
- No Churn

---

## Success Criteria

The project is considered successful if it helps the business identify customers who are likely to leave early enough for the company to take actions that improve customer retention.


# 📊 Telecom Customer Churn Prediction System

An end-to-end Machine Learning solution designed to predict customer churn in the telecommunications industry. This project spans from exploratory data analysis and leakage-free feature engineering to training a deep PyTorch neural network, serving real-time predictions via Flask, and packaging the system into a standalone Windows Desktop Application installer.

---

## 🚀 Key Highlights & Architectural Features

- **Leakage-Free Pipeline**: Features are scaled and encoded using a unified Scikit-Learn `ColumnTransformer` fitted strictly on training data.
- **PyTorch Inference Engine**: Custom neural network utilizing Dropout and Sigmoid activation for calibrated churn probability estimation.
- **Desktop Application Architecture**: Bundled as a standalone Windows GUI utilizing `pywebview` and a local Flask backend service.
- **Enterprise-Grade Packaging**: Built using PyInstaller (`onedir`) and packaged via Inno Setup 7, bundling the Microsoft Visual C++ Redistributable (`vc_redist.x64.exe`) to resolve dynamic runtime dependencies (`WinError 126`) automatically on target machines.

---

## 🧠 Machine Learning Architecture

### 1. Feature Engineering
Before passing raw data to the transformation pipeline, the system extracts critical behavioral signals:
- **`TotalServices`**: Count of enrolled supplementary services (`OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`).
- **`IsAutomaticPayment`**: Binary flag indicating automatic payment methods (`Bank transfer (automatic)` or `Credit card (automatic)`).
- **`MonthlySpendDiff`**: Difference between current monthly charges and tenure-normalized total spend:
  $$\text{MonthlySpendDiff} = \text{MonthlyCharges} - \frac{\text{TotalCharges}}{\text{tenure} + 1}$$

### 2. PyTorch Model Architecture
The final neural network model consists of:
- **Input Layer**: 33 preprocessed features (continuous variables standard-scaled; nominal categories one-hot encoded with `drop='first'`).
- **Hidden Layer**: `Linear(33 → 4)` with `ReLU` activation and `Dropout(p=0.4)`.
- **Output Layer**: `Linear(4 → 1)` with `Sigmoid` activation delivering churn probability $[0, 1]$.

---

## 📁 Repository Structure

```text
customer-churn-prediction-system/
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Raw benchmark dataset
│   └── processed/                            # Preprocessed & split datasets
├── models/
│   ├── preprocessor_pipeline.pkl             # Scikit-Learn preprocessor pipeline
│   └── churn_nn_weights.pth                  # Trained PyTorch model weights
├── notebooks/
│   ├── 01_business_and_eda.ipynb             # Exploratory Data Analysis & business KPI design
│   ├── 02_cleaning_and_feature_engineering.ipynb # Leakage-free feature design & baseline validation
│   └── 03_preprocessing_and_modeling.ipynb   # Model training & PyTorch convergence
├── templates/
│   └── UI.html                               # Frontend dashboard & scoring form
├── app.py                                    # Flask prediction service & API contract
├── desktop_app.py                            # GUI window manager via pywebview
├── CustomerChurnPredictor.spec               # PyInstaller specification profile
├── CustomerChurnPredictor.iss                # Inno Setup 7 installer compiler script
├── requirements.txt                          # Project runtime dependencies
└── README.md