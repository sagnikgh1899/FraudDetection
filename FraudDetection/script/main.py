import csv
import pandas as pd
import io
import json
import os
import sys

from flask import Flask, request, render_template, session, Response

sys.path.append("../models")
from lof import lof_anomaly_detection
from knn import knn_anomaly_detection
from copod import copod_anomaly_detection
from abod import abod_anomaly_detection
from ecod import ecod_anomaly_detection

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
    with open('models_performance.json') as f:
        models = json.load(f)
    best_model = None
    return render_template('user-page.htm', models=models, best_model=best_model)


@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    with open('models_performance.json') as f:
        models = json.load(f)
    best_model = None
    best_f1 = -1
    best_mcc = -1
    best_time = float('inf')
    for model_name, model_details in models.items():
        precision = model_details['precision']
        recall = model_details['recall']
        f1 = model_details['f1']
        mcc = model_details['mcc']
        time = model_details['time']
        if f1 >= best_f1 and mcc >= best_mcc and time < best_time:
            best_f1 = f1
            best_mcc = mcc
            best_time = time
            best_model = model_name
        elif f1 >= best_f1 and mcc >= best_mcc:
            best_f1 = f1
            best_mcc = mcc
            best_time = time
            best_model = model_name
        elif f1 >= best_f1 and time < best_time:
            best_f1 = f1
            best_mcc = mcc
            best_time = time
            best_model = model_name
        elif mcc >= best_mcc and time < best_time:
            best_f1 = f1
            best_mcc = mcc
            best_time = time
            best_model = model_name
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
    return render_template('user-page.htm', models=models, best_model=best_model, filepath=filepath)


@app.route('/download-csv', methods=['POST'])
def download_csv():
    filepath = session.get('filepath')
    if filepath is None or not os.path.exists(filepath):
        return 'File not found', 404

    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(filepath)

    # Detect anomalies in the data using the ECOD algorithm
    outliers = ecod_anomaly_detection(data, 0.055)
    fraud = data[outliers].reset_index(drop=True)

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


if __name__ == '__main__':
    app.run(debug=True)
