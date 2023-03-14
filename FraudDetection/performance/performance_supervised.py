"""
This module prints the performance of the fraud detection models
as present on the models_performance.json file
"""
import sys
import os
import time
import pandas as pd

sys.path.append(os.path.abspath("./FraudDetection/models"))

# pylint: disable=C0413
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score, recall_score, f1_score, matthews_corrcoef


def read_data():
    """
    Function to read csv files
    parameters: None
    return: Preprocessed data from fraud, beneficiary, inpatient, outpatient.
    raise FileExistsError: raises an exception when file is not found
    """
    try:
        preprocessed = pd.read_csv("./FraudDetection/data/preprocessed.csv")
        return preprocessed
    except FileExistsError as error:
        raise error


def compute_performance_metrics(model_to_test, X_train, X_test, y_train, y_test):
    """
    Computes the performance metrics for the given model and test data.
    Args:
        model_to_test: The fraud detection model to evaluate.
        x_test: The test data to evaluate.
        y_test: The true labels for the test data.
    Returns:
        A dictionary with the computed performance metrics.
    """


    start_time = time.time()
    x_test = x_test.astype('float64')
    y_pred = model_to_test(x_test)
    end_time = time.time()
    precision = round(precision_score(y_test, y_pred), 3)
    recall = round(recall_score(y_test, y_pred), 3)
    f1_value = round(f1_score(y_test, y_pred), 3)
    mcc = round(matthews_corrcoef(y_test, y_pred), 3)
    total_time = round((end_time - start_time), 3)
    performance_dict = {
        "precision": precision,
        "recall": recall,
        "f1": f1_value,
        "mcc": mcc,
        "time": total_time
    }
    return performance_dict


if __name__ == '__main__':

    models = {
        "LR": Logistic Regression,
        "RF": Random Forest,
    }

    # Provide the paths to the preprocessed dataset and the actual labels
    fraud_data = read_data()
    x_data = fraud_data.drop(columns='PotentialFraud')
    y_labels = fraud_data['PotentialFraud']

    # Replace and Drop NA cols
    x_data['DeductibleAmtPaid'] = x_data['DeductibleAmtPaid'].fillna(0)
    x_data.dropna(axis=1, inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(x_data , y_labels, 
                                                        shuffle = True, 
                                                        test_size=0.3, 
                                                        random_state=1)

    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)

    y_pred = logreg.predict(X_test)

    print(classification_report(y_test, y_pred))
    
#     performance = {}
#     for model_name, model in models.items():
#         print(f"Computing performance for {model_name}...")
#         performance[model_name] = compute_performance_metrics(model, X_train, X_test, y_train, y_test)

# print("\n\n")
# for model_name, model_performance in performance.items():
#     print(model_name, model_performance)
