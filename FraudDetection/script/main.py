import csv
import pandas as pd
import io
import json
import os
import sys
import time

from flask import Flask, request, render_template, session, Response
from sklearn.metrics import precision_score, recall_score, f1_score, matthews_corrcoef

sys.path.append("../models")
from lof import lof_anomaly_detection
from knn import knn_anomaly_detection
from copod import copod_anomaly_detection
from abod import abod_anomaly_detection
from ecod import ecod_anomaly_detection

######
# Write a function that takes in the models and then creates the models_performance.json
# file, which is a dictionary of dictionaries in the order - Model Name: precision, recall, f1, mcc, time.
# The file should be stored in a folder 'json' in the same directory as main.py
JSON_FILES = 'json'
if not os.path.exists(JSON_FILES):
    os.makedirs(JSON_FILES)


def compute_model_performance(fraud_detection_models, x_test_file, y_test_file, filename="models_performance.json"):
    """
    Computes the performance metrics for each model and stores the values in a JSON file.

    Args:
    models: A dictionary of model names to PyOD models to compute performance metrics for.
    X_test_file: A string containing the filename of the csv file containing the test data.
    y_test_file: A string containing the filename of the csv file containing the true labels for the test data.
    filename: The name of the JSON file to save the performance metrics.
    """
    performance = {}

    # Load test data from csv files
    x_test = pd.read_csv(x_test_file)
    y_test = pd.read_csv(y_test_file)

    for model_name, model in fraud_detection_models.items():
        print(f"Computing performance for {model_name}...")
        start_time = time.time()
        x_test = x_test.astype('float64')
        y_pred = model(x_test)
        end_time = time.time()

        precision = round(precision_score(y_test, y_pred), 3)
        recall = round(recall_score(y_test, y_pred), 3)
        f1 = round(f1_score(y_test, y_pred), 3)
        mcc = round(matthews_corrcoef(y_test, y_pred), 3)
        total_time = round((end_time - start_time), 3)

        performance[model_name] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "mcc": mcc,
            "time": total_time
        }

    filepath = os.path.join(JSON_FILES, filename)
    with open(filepath, 'w') as f:
        json.dump(performance, f)
    # with open(filename, "w") as f:
    #     json.dump(performance, f)

    # print(f"Performance metrics saved to {filepath}")


def define_models(data_model_performance, correct_labels):
    models = {
        "LOF": lof_anomaly_detection,
        "KNN": knn_anomaly_detection,
        "COPOD": copod_anomaly_detection,
        "ABOD": abod_anomaly_detection,
        "ECOD": ecod_anomaly_detection
    }
    compute_model_performance(models, data_model_performance, correct_labels)


UPLOAD_DIR = 'uploads'

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app = Flask(__name__, template_folder=os.path.abspath('../templates'), static_folder=os.path.abspath('../static'))

# Set the session key and type
app.secret_key = 'my_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the app with the session object
app.config.from_object(__name__)


@app.route('/')
def home():
    return render_template('start-page.htm')


@app.route('/home-page')
def home_page():
    return render_template('start-page.htm')


@app.route('/user-page')
def user_page():
    filepath = os.path.join(JSON_FILES, 'models_performance.json')
    with open(filepath) as f:
        models = json.load(f)
    try:
        best_model_name = session.get('best_model_name')
    except:
        best_model_name = None
    return render_template('user-page.htm', models=models, best_model=best_model_name)


@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    filepath = os.path.join(JSON_FILES, 'models_performance.json')
    with open(filepath) as f:
        models = json.load(f)
    best_model_name = None
    best_f1 = -1
    best_mcc = -1
    best_time = float('inf')
    for model_name, model_details in models.items():
        # precision = model_details['precision']
        # recall = model_details['recall']
        f1 = model_details['f1']
        mcc = model_details['mcc']
        time_to_predict = model_details['time']
        print(model_name, f1, mcc, time_to_predict)

        count_improvement = 0
        if f1 > best_f1:
            count_improvement += 1
        if mcc > best_mcc:
            count_improvement += 1
        if time_to_predict < best_time:
            count_improvement += 1
        if count_improvement >= 2:
            best_f1 = f1
            best_mcc = mcc
            best_time = time_to_predict
            best_model_name = model_name

        # if f1 >= best_f1 and mcc >= best_mcc and time_to_predict < best_time:
        #     best_f1 = f1
        #     best_mcc = mcc
        #     best_time = time_to_predict
        #     best_model_name = model_name
        # elif f1 >= best_f1 and mcc >= best_mcc:
        #     best_f1 = f1
        #     best_mcc = mcc
        #     best_time = time_to_predict
        #     best_model_name = model_name
        # elif f1 > best_f1 and time_to_predict < best_time:
        #     best_f1 = f1
        #     best_mcc = mcc
        #     best_time = time_to_predict
        #     best_model_name = model_name
        # elif mcc > best_mcc and time_to_predict < best_time:
        #     best_f1 = f1
        #     best_mcc = mcc
        #     best_time = time_to_predict
        #     best_model_name = model_name
    if 'csv-file' not in request.files:
        return 'No file selected'
    file = request.files['csv-file']
    if file.filename == '':
        return 'No file selected'
    contents = file.read().decode('utf-8')
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, 'w') as f:
        f.write(contents)
    session['filepath'] = filepath
    session['best_model_name'] = best_model_name
    session['models'] = models
    return render_template('user-page.htm', models=models, best_model=best_model_name, filepath=filepath)


@app.route('/download-csv', methods=['POST'])
def download_csv():
    filepath = session.get('filepath')
    best_model_name = session.get('best_model_name')
    deployed_model = None
    print("F1", best_model_name)
    if best_model_name == "LOF":
        deployed_model = lof_anomaly_detection
    elif best_model_name == "KNN":
        deployed_model = knn_anomaly_detection
    elif best_model_name == "COPOD":
        deployed_model = copod_anomaly_detection
    elif best_model_name == "ABOD":
        deployed_model = abod_anomaly_detection
    elif best_model_name == "ECOD":
        deployed_model = ecod_anomaly_detection
    # if best_model_name == "LOF":
    #   deployed_model = lof_anomaly_detection
    if filepath is None or not os.path.exists(filepath):
        return 'File not found', 404

    # Read the CSV file into a pandas DataFrame
    new_test_data = pd.read_csv(filepath)

    if deployed_model is not None:
        # Detect anomalies in the data using the best_model algorithm
        outliers = deployed_model(new_test_data)
        fraud = new_test_data[outliers].reset_index(drop=True)

        # Create a StringIO object to write the fraud data as a CSV file
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(fraud.columns)  # Write the column headers
        writer.writerows(fraud.values)  # Write the rows of data

        # Set the HTTP headers to indicate a CSV file download
        headers = {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=fraudulent_claims.csv'
        }

        # Return the CSV file as a response object
        return Response(output.getvalue(), headers=headers)

    else:
        models = session.get('models')
        return render_template('user-page.htm', models=models, best_model=best_model_name)


if __name__ == '__main__':
    data_for_model_performance_file = "lympho(data).csv"  # Provide the preprocessed dataset
    actual_labels_file = "lympho(gt).csv"
    define_models(data_for_model_performance_file, actual_labels_file)
    app.run(debug=True)
