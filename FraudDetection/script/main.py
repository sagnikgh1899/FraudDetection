import pandas as pd
import io
import json
from flask import Flask, request, render_template, jsonify
import os
import sys

sys.path.append("../models")
from lof import lof_anomaly_detection
from knn import knn_anomaly_detection
from copod import copod_anomaly_detection
from abod import abod_anomaly_detection
from ecod import ecod_anomaly_detection
# from Suod import SUOD_anomaly_detection
# from knn import knn_anomaly_detection
# from knn import knn_anomaly_detection

app = Flask(__name__, template_folder=os.path.abspath('../templates'), static_folder=os.path.abspath('../static'))


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
    return render_template('user-page.htm', models=models)


@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'csv-file' not in request.files:
        return 'No file selected'
    file = request.files['csv-file']
    if file.filename == '':
        return 'No file selected'
    contents = file.read().decode('utf-8')
    data = pd.read_csv(io.StringIO(contents))
    outliers = ecod_anomaly_detection(data, 0.055)
    fraud = data[outliers].reset_index(drop=True)
    non_fraud = data[~outliers].reset_index(drop=True)
    print(fraud.shape)
    print(non_fraud.shape)
    print(outliers.shape)
    return render_template('user-page.htm', fraud=fraud.to_html(),
                           non_fraud=non_fraud.to_html())


if __name__ == '__main__':
    app.run(debug=True)
