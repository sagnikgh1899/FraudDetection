import pandas as pd
import io
import json
import os
from flask import Flask, request, render_template, jsonify
#import sys
#sys.path.append('../models')
from lof_anomaly import lof_anomaly_detection
from check_password import check_password
#sys.path.append('../')

app = Flask(__name__)

CORRECT_PASSWORD = '12345'


@app.route('/')
def home():
    return render_template('start-page.htm')


@app.route('/home-page')
def home_page():
    return render_template('start-page.htm')


@app.route('/user-page')
def user_page():
    return render_template('user-page.htm')


@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'csv-file' not in request.files:
        return 'No file selected'
    file = request.files['csv-file']
    if file.filename == '':
        return 'No file selected'  # render_template('home.html')
    contents = file.read().decode('utf-8')
    # Do something with the contents of the CSV file
    data = pd.read_csv(io.StringIO(contents))
    outliers = lof_anomaly_detection(data, 0.05)
    fraud = data[outliers].reset_index(drop=True)
    non_fraud = data[~outliers].reset_index(drop=True)
    print(fraud.shape)
    print(non_fraud.shape)
    print(outliers.shape)
    # return render_template('user-page.htm', fraud=fraud.to_html(), non_fraud=non_fraud.to_html())
    return render_template('user-page.htm', fraud=fraud.to_html(),
                           non_fraud=non_fraud.to_html())

    # print(df.head())
    # return 'Uploaded CSV file'


@app.route('/dev-page', methods=['GET', 'POST'])
def dev_page():
    if request.method == 'POST':
        password = request.form['password']
        if check_password(password, CORRECT_PASSWORD):
            return render_template('dev-page.htm')
        else:
            error = 'Invalid password'
            return render_template('password.htm', error=error)
    else:
        return render_template('password.htm')


@app.route('/main.py', methods=['GET'])
def handle_request():
    # Define the path to the selected_models.json file
    file_path = "./selected_models.json"
    # Check if the file exists
    if not os.path.exists(file_path):
        # If the file does not exist, create an empty list and write it to the file
        with open(file_path, "w") as f:
            json.dump([], f)

    action = request.args.get('action')
    if action == 'save_selected_models':
        selected_models = request.args.getlist('selected_models')
        # Convert the received string into an array of strings
        selected_models = [model.strip() for model in selected_models[0].split(',')]
        with open('selected_models.json', 'w') as f:
            json.dump(selected_models, f)
        return jsonify(success=True)
    elif action == 'get_selected_models':
        try:
            with open('selected_models.json', 'r') as f:
                selected_models = json.load(f)
            return jsonify(selected_models=selected_models)
        except FileNotFoundError:
            return jsonify(selected_models=None)
    else:
        return jsonify(success=False)


if __name__ == '__main__':
    app.run(debug=True)
