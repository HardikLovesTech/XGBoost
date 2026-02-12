# Project Overview And Explaination
This is a github repository that contains the implementation of XGBoost regression and classification(coming soon) . So all of us think how does XGBoost actualy work right?
So XGBoost basically means - Extreme Gradient Boost. We make trees and try to calculate Similarity Score
## Similarity Score
Similarity score measures the quality of residuals within a leaf. When residuals are very different , they cancel each other out , resulting in a smaller similarity score

## Gain Calculation
The gain quantifies how much better a split clusters similar residuals compared to the root. The goal is to find the threshold that yields the largest gain

## Tree Pruning
XGBoost trees are pruned based on gain values and a paramter called _gamma_ . If the difference between the gaiin of a branch and gamma is negative, the branch is removed.

## Regularization with Lambda
The _Lambda_ paramter is a regularization paramter that reduces prediction sensitivity to indivisual observations. A higher _Lambda_ value leads to smaller similarity score and more aggresive pruning.

# Problem Statement
"Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]



# Dataset Description
Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:

Customers who left within the last month – the column is called Churn
Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
Demographic info about customers – gender, age range, and if they have partners and dependents

# Model Used – XGBoost
Here there is no specific reason to use XGBoost but to apply it by yourself and to get a hands-on-experience so that we get to know what are we actually heading too...!!!

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

'''
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
'''


# Exploratory Data Analysis (EDA)

# Data Preprocessing
The following preprocessing steps were applied before model training:
- Missing values were identified and handled appropriately.
- Categorical variables were encoded using suitable encoding techniques.
- Numerical features were validated for outliers and distribution issues.
- The dataset was checked for class imbalance.
- Features and target variable were separated.

These steps ensured that the data was suitable for training the XGBoost model.

# Feature Engineering


# Train–Test Split Strategy
The dataset was split into training and testing sets using an 80–20 ratio.
Random seed: 42
Stratified split was used (for classification problems) to maintain class distribution consistency.
This ensures reproducibility and fair model evaluation.

# Model Training
An XGBoost model was initialized and trained on the training dataset.
Objective function: __binary:logistic__ (for binary classification)
Evaluation metric: __logloss__
Random state: 42
The model was trained using default parameters initially to establish a baseline performance.

# Hyperparameter Tuning
Hyperparameter tuning was performed using GridSearchCV with 5-fold cross-validation.
The following parameters were tuned
- max_depth
- learning_rate
- n_estimators
- subsample
The best combination of hyperparameters was selected based on balanced accuracy score.
This improved generalization and reduced overfitting.


# References
XGBoost Official Documentation
Scikit-learn Documentation
Original XGBoost Research Paper

# Author
Hardik Runwal
