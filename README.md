# Project Overview And Explanation
This is a GitHub repository containing an implementation of XGBoost for regression and classification tasks. XGBoost, which stands for Extreme Gradient Boosting, works by building trees and calculating similarity scores to optimize model performance.

## Similarity Score
Similarity score measures the quality of residuals within a leaf. When residuals are very different, they cancel each other out, resulting in a smaller similarity score.

## Gain Calculation
Gain quantifies how much better a split clusters similar residuals compared to the root. The goal is to find the threshold that yields the largest gain.

## Tree Pruning
XGBoost trees are pruned based on gain values and a parameter called gamma. If the difference between the gain of a branch and gamma is negative, the branch is removed.

## Regularization with Lambda
The Lambda parameter is a regularization parameter that reduces prediction sensitivity to individual observations. A higher Lambda value leads to smaller similarity scores and more aggressive pruning.

# Problem Statement
Predict customer churn behavior to develop focused customer retention programs. [IBM Sample Data Sets]

# Dataset Description
Each row represents a customer, with columns containing customer attributes. The dataset includes:
- Churn status (customers who left within the last month)
- Services: phone, internet, online security, online backup, device protection, tech support, streaming TV and movies
- Account information: contract type, payment method, billing, monthly and total charges
- Demographics: gender, age range, partner and dependent status

# Model Used – XGBoost
XGBoost was selected to provide hands-on experience with gradient boosting techniques and understand their application in customer churn prediction.

# Installation
1. Ensure Python 3.10+ is installed.
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   (Linux/Mac)
venv\Scripts\activate      (Windows)
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

# Project Structure
```
└── XGBoost/
   ├── .gitattributes
   ├── README.md
   ├── TelcoChurnDataset.csv
   ├── Telco_customer_churn.csv
   ├── Telco_customer_churn.xlsx
   ├── XGBoost.ipynb
   ├── archive/
   │   └── Telco_customer_churn.xlsx
   ├── archive.zip
   ├── requirements.txt
   └── training.py
```

# Exploratory Data Analysis (EDA)

# Data Preprocessing
The following preprocessing steps were applied before model training:
- Identified and handled missing values appropriately
- Encoded categorical variables using suitable techniques
- Validated numerical features for outliers and distribution issues
- Checked dataset for class imbalance
- Separated features and target variable

# Feature Engineering

# Train–Test Split Strategy
- Dataset split: 80–20 ratio
- Random seed: 42
- Stratified split to maintain class distribution consistency
- Ensures reproducibility and fair model evaluation

# Model Training
- Objective function: binary:logistic (for binary classification)
- Evaluation metric: logloss
- Random state: 42
- Trained using default parameters initially to establish baseline performance

# Hyperparameter Tuning
Hyperparameter tuning was performed using GridSearchCV with 5-fold cross-validation.
Parameters tuned:
- max_depth
- learning_rate
- n_estimators
- subsample

Best hyperparameters were selected based on balanced accuracy score to improve generalization and reduce overfitting.

# References
- XGBoost Official Documentation
- Scikit-learn Documentation
- Original XGBoost Research Paper

# Author
Hardik Runwal
