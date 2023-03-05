"""
Main module that comprises of the Flask App for hosting the webpage,
along with the fraud analysis
"""
import csv
import time
import sys
import os
import json
import io
import pandas as pd
from flask import Flask, request, render_template, session, Response
from sklearn.metrics import precision_score, recall_score, f1_score, matthews_corrcoef

sys.path.append(os.path.abspath("../models"))
# pylint: disable=C0413
from models import lof_anomaly_detection
from models import knn_anomaly_detection
from models import copod_anomaly_detection
from models import abod_anomaly_detection
from models import ecod_anomaly_detection


def create_directory_if_not_exists(directory):
    """
    Create a directory if it does not exist.
    Args:
        directory (str): The name of the directory to be created.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


JSON_FILES = 'json'
create_directory_if_not_exists(JSON_FILES)


def compute_performance_metrics(model, x_test, y_test):
    """
    Computes the performance metrics for the given model and test data.
    Args:
        model: The fraud detection model to evaluate.
        x_test: The test data to evaluate.
        y_test: The true labels for the test data.
    Returns:
        A dictionary with the computed performance metrics.
    """
    start_time = time.time()
    x_test = x_test.astype('float64')
    y_pred = model(x_test)
    end_time = time.time()
    precision = round(precision_score(y_test, y_pred), 3)
    recall = round(recall_score(y_test, y_pred), 3)
    f1_value = round(f1_score(y_test, y_pred), 3)
    mcc = round(matthews_corrcoef(y_test, y_pred), 3)
    total_time = round((end_time - start_time), 3)
    performance = {
        "precision": precision,
        "recall": recall,
        "f1": f1_value,
        "mcc": mcc,
        "time": total_time
    }
    return performance


def compute_model_performance(fraud_detection_models, x_test_file, y_test_file,
                              filename="models_performance.json"):
    """
    Computes the performance metrics for each model and stores the values in a JSON file.
    Args:
        fraud_detection_models : A dictionary of model names to compute performance metrics.
        x_test_file : Filename of the csv file containing the test data.
        y_test_file : Filename of the csv file containing the true labels for the test data.
        filename : The name of the JSON file to save the performance metrics.
    """
    performance = {}
    x_test = pd.read_csv(x_test_file)
    y_test = pd.read_csv(y_test_file)
    for model_name, model in fraud_detection_models.items():
        print(f"Computing performance for {model_name}...")
        performance[model_name] = compute_performance_metrics(model, x_test, y_test)
    filepath = os.path.join(JSON_FILES, filename)
    with open(filepath, 'w', encoding='utf-8') as fname:
        json.dump(performance, fname)


def define_models(data_model_performance: dict, correct_labels: pd.Series):
    """
    Define a dictionary of anomaly detection models and compute their performance.
    Args:
        data_model_performance : A dictionary containing data frames with the models' performance.
        correct_labels : A pandas series with the correct labels for the data.
    Returns:
        None.
    """
    models = {
        "LOF": lof_anomaly_detection,
        "KNN": knn_anomaly_detection,
        "COPOD": copod_anomaly_detection,
        "ABOD": abod_anomaly_detection,
        "ECOD": ecod_anomaly_detection
    }
    compute_model_performance(models, data_model_performance, correct_labels)


UPLOAD_DIR = 'uploads'
create_directory_if_not_exists(UPLOAD_DIR)

app = Flask(__name__, template_folder=os.path.abspath('../templates'),
            static_folder=os.path.abspath('../static'))

app.secret_key = 'my_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'


def initialize_app(application):
    """
    Initializes the Flask app with the session object.
    Args:
        application (Flask): The Flask app object to be initialized.
    """
    application.config.from_object(__name__)


initialize_app(app)


@app.route('/')
def home():
    """
    Renders the start page HTML template.
    Returns:
        str: The rendered HTML template.
    """
    return render_template('start-page.htm')


@app.route('/home-page')
def home_page():
    """
    Renders the start page.
    Returns:
        A rendered HTML template.
    """
    return render_template('start-page.htm')


@app.route('/user-page')
def user_page():
    """
    Render the user page, which displays the performance of the models.
    Returns:
        str: The HTML content to be displayed on the user page.
    """
    filepath = os.path.join(JSON_FILES, 'models_performance.json')
    with open(filepath, encoding='utf-8') as fname:
        models = json.load(fname)
    try:
        best_model_name = session.get('best_model_name')
    except ValueError:
        best_model_name = None
    return render_template('user-page.htm', models=models, best_model=best_model_name)


@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    """
    Uploads a CSV file and displays the best performing model on the user page.
    Returns:
        str: A message indicating whether a file was uploaded or not.
    """
    filepath = os.path.join(JSON_FILES, 'models_performance.json')
    with open(filepath, encoding='utf-8') as fname:
        models = json.load(fname)
    best_model_name = None
    best_f1 = -1
    best_mcc = -1
    best_time = float('inf')
    for model_name, model_details in models.items():
        f1_value = model_details['f1']
        mcc = model_details['mcc']
        time_to_predict = model_details['time']
        # print(model_name, f1, mcc, time_to_predict)
        count_improvement = 0
        if f1_value > best_f1:
            count_improvement += 1
        if mcc > best_mcc:
            count_improvement += 1
        if time_to_predict < best_time:
            count_improvement += 1
        if count_improvement >= 2:
            best_f1 = f1_value
            best_mcc = mcc
            best_time = time_to_predict
            best_model_name = model_name
    if 'csv-file' not in request.files:
        return 'No file selected'
    file = request.files['csv-file']
    if file.filename == '':
        return 'No file selected'
    contents = file.read().decode('utf-8')
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, 'w', encoding='utf-8') as fname:
        fname.write(contents)
    session['filepath'] = filepath
    session['best_model_name'] = best_model_name
    session['models'] = models
    return render_template('user-page.htm', models=models, best_model=best_model_name,
                           filepath=filepath)


@app.route('/download-csv', methods=['POST'])
def download_csv():
    """
    Detects anomalies using the deployed model and returns CSV file of the fraudulent claims.
    Returns:
        flask.Response: The HTTP response containing the fraudulent claims in a CSV file.
    """
    filepath = session.get('filepath')
    best_model_name = session.get('best_model_name')
    deployed_model = None
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
    if filepath is None or not os.path.exists(filepath):
        return 'File not found', 404
    new_test_data = pd.read_csv(filepath)
    if deployed_model is not None:
        outliers = deployed_model(new_test_data)
        fraud = new_test_data[outliers].reset_index(drop=True)
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(fraud.columns)
        writer.writerows(fraud.values)
        headers = {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=fraudulent_claims.csv'
        }
        return Response(output.getvalue(), headers=headers)

    models = session.get('models')
    return render_template('user-page.htm', models=models, best_model=best_model_name)


def run_model_performance_evaluation(data_file, labels_file):
    """
    Run the model performance evaluation using preprocessed data and actual labels.
    Args:
        data_file (str): The path to the preprocessed dataset file.
        labels_file (str): The path to the file containing the actual labels.
    Returns:
        None
    """
    define_models(data_file, labels_file)
    app.run(debug=True)


if __name__ == '__main__':
    # Provide the paths to the preprocessed dataset and the actual labels
    DATA_FILE = "lympho(data).csv"
    LABELS_FILE = "lympho(gt).csv"

    # Run the model performance evaluation
    run_model_performance_evaluation(DATA_FILE, LABELS_FILE)
