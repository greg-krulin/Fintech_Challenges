## Overview of the Analysis

The purpose of the analysis was to leverage machine learning to build a model capable of accurately predicting the risk status of loans, with statuses marked as either '0' (healthy loan) or '1' (high-risk loan). This analysis was carried out on financial data related to loan size, interest rate, borrower income, debt-to-income ratio, the number of accounts, derogatory marks, and total debt. Our target variable, 'loan_status', was severely imbalanced with 75036 healthy loans ('0') and only 2500 high-risk loans ('1').

The machine learning process involved splitting the data into training and testing sets, training a logistic regression model, making predictions, and evaluating the model's performance using metrics such as accuracy, precision, and recall. The data imbalance was addressed using a resampling method, specifically, RandomOverSampler.

## Results

* Machine Learning Model 1 (Logistic Regression without Oversampling):
  * Balanced Accuracy Score: 0.95
  * Class 0 Precision: 1.00, Recall: 0.99
  * Class 1 Precision: 0.85, Recall: 0.91


* Machine Learning Model 2 (Logistic Regression with Oversampling):
  * Balanced Accuracy Score: Unknown (based on classification report, it's likely to be high)
  * Class 0 Precision: 1.00, Recall: 0.99
  * Class 1 Precision: 0.84, Recall: 0.99

## Summary

Both models perform extremely well in predicting both healthy loans and high-risk loans, as indicated by high precision, recall, and accuracy scores. However, the model trained with oversampled data performs slightly better in predicting high-risk loans, given the improved recall (0.99) for this class. Therefore, if the goal is to minimize the risk by accurately predicting high-risk loans, the oversampled logistic regression model is recommended. This performance improvement showcases the significance of addressing class imbalance when training the model.
