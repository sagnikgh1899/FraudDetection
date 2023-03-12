"""
Main module that comprises of the Flask App for hosting the webpage,
along with the fraud analysis
"""
import csv
import sys
import os
import json
import io
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, session, Response

sys.path.append(os.path.abspath("./FraudDetection/models"))

# pylint: disable=C0413
# pylint: disable=R1735
import plotly
#import plotly.express as px
import plotly.graph_objects as go
from models import loda_anomaly_detection
from models import ecod_anomaly_detection
from models import copod_anomaly_detection
from models import iforest_anomaly_detection
from models import suod_anomaly_detection


def read_data():
    """
    Function to read csv files
    parameters: None
    return: Preprocessed data from fraud, beneficiary, inpatient, outpatient.
    raise FileExistsError: raises an exception when file is not found
    """
    try:
        preprocessed=pd.read_csv("data/preprocessed.csv")
        return preprocessed
    except FileExistsError as error:
        raise error

def create_directory_if_not_exists(directory):
    """
    Create a directory if it does not exist.
    Args:
        directory (str): The name of the directory to be created.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def state_wise_visualization(inpatient_final_df,state_mapping):
    """
    Computes the state wise distribution of frauds.
    Args:
        inpatient_final_df : Dataframe have preprocessed data.
        state_mapping : Dataframe having state code to state name mapping.
    """
    grouped = pd.pivot_table(inpatient_final_df.groupby(
        ['PotentialFraud','Abbreviation'])['BeneID'].count().reset_index(),
        values = 'BeneID', index=['Abbreviation'],
        columns = 'PotentialFraud').reset_index()
    grouped.reset_index(drop = True)
    grouped.fillna(0,inplace=True)
    grouped['Total'] = grouped['No'] + grouped['Yes']
    grouped['% Frauds'] = grouped['Yes']*100/grouped['Total']
    grouped.sort_values(by = ['% Frauds'],inplace=True, ascending = False)
    grouped.loc[grouped['Total'] > 100].head(10)
    grouped = grouped[['Abbreviation','% Frauds']]
    grouped.fillna(0,inplace=True)
    grouped = grouped.merge(state_mapping, on = 'Abbreviation',how = 'inner')
    grouped['% Frauds'] = grouped['% Frauds'].apply(lambda x: round(x,1))
    fig = go.Figure(data=go.Choropleth(
             locations=grouped['Abbreviation'],
             z=grouped['% Frauds'].astype(float),
             locationmode='USA-states',
             colorscale="Viridis_r",
             autocolorscale=False,
             text=grouped['State_Name'], # hover text
             marker_line_color='white', # line markers between states
        ))


    fig.update_layout(
        title_text = '% of Frauds by State',
        geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(255, 255, 255)'),
        )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

def eda(state_mapping):
    """
    Creates preprocessed data.
    Args:
        state_mapping : Dataframe having state code to state name mapping.
    """
    pd.set_option('display.max_columns', None)
    fraud_providers = pd.read_csv('data/Train-1542865627584.csv')
    beneficiary = pd.read_csv('data/Train_Beneficiarydata-1542865627584.csv')
    inpatient = pd.read_csv("data/Train_Inpatientdata-1542865627584.csv")
    #outpatient = pd.read_csv("data/Train_Outpatientdata-1542865627584.csv")
    inpatient_intermediate_df = pd.merge(inpatient,beneficiary,
        on = ['BeneID'], how = 'inner')
    inpatient_final_df = pd.merge(inpatient_intermediate_df,fraud_providers,
        on = ['Provider'], how  = 'inner')
    inpatient_final_df['DischargeDt'] = inpatient_final_df['DischargeDt'].apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d'))
    inpatient_final_df['AdmissionDt'] = inpatient_final_df['AdmissionDt'].apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d'))
    inpatient_final_df['ClaimStartDt'] = inpatient_final_df['ClaimStartDt'].apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d'))
    inpatient_final_df['ClaimEndDt'] = inpatient_final_df['ClaimEndDt'].apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d'))
    inpatient_final_df['DOB'] = inpatient_final_df['DOB'].apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d'))
    inpatient_final_df['Day_admitted'] = (inpatient_final_df['DischargeDt']-
    inpatient_final_df['AdmissionDt'])
    inpatient_final_df['Day_admitted'] = inpatient_final_df['Day_admitted'].apply(
        lambda x: x.days)
    inpatient_final_df['Age'] = inpatient_final_df['DOB'].apply(
        lambda x: datetime.strptime("2013-03-03", '%Y-%m-%d').year - x.year)
        #inpatient_final_df['Age']
    inpatient_final_df = inpatient_final_df.merge(state_mapping, on ='State', how = 'left')
    inpatient_final_df['Day_admitted'] = (inpatient_final_df['DischargeDt'] -
         inpatient_final_df['AdmissionDt'])
    inpatient_final_df['Day_admitted'] = inpatient_final_df['Day_admitted'].apply(
         lambda x: x.days)
    inpatient_final_df['Age'] = inpatient_final_df['DOB'].apply(
         lambda x: datetime.strptime("2013-03-03", '%Y-%m-%d').year - x.year)
    inpatient_final_df.loc[(inpatient_final_df['Day_admitted'] <= 20),
         "Days_Admitted_Bucket"] = "0-20 Days"
    inpatient_final_df.loc[((inpatient_final_df['Day_admitted'] > 20)),
         "Days_Admitted_Bucket"] = "More than 20 Days"
    inpatient_final_df.loc[inpatient_final_df['InscClaimAmtReimbursed']<=20000,
         'InscClaimAmtReimbursed_Bucket'] = '0 - 20000'
    inpatient_final_df.loc[((inpatient_final_df['InscClaimAmtReimbursed'] > 20000) &
         (inpatient_final_df['InscClaimAmtReimbursed']<=40000)),
         'InscClaimAmtReimbursed_Bucket'] = '20000 - 40000'
    inpatient_final_df.loc[((inpatient_final_df['InscClaimAmtReimbursed'] > 40000)
         & (inpatient_final_df['InscClaimAmtReimbursed']<=60000)),
         'InscClaimAmtReimbursed_Bucket'] = '40000 - 60000'
    inpatient_final_df.loc[inpatient_final_df['InscClaimAmtReimbursed']> 60000,
         'InscClaimAmtReimbursed_Bucket'] = 'Greater than 60000'
    return inpatient_final_df

def first_visualization(inpatient_final_df):
    """
    Creates a visualization for the trend observed in number of days admitted.
    Args:
        inpatient_final_df : Dataframe have preprocessed data.
    """
    grouped = pd.pivot_table(inpatient_final_df.groupby(
         ['PotentialFraud','Days_Admitted_Bucket'])['BeneID'].count().
         reset_index(), values = 'BeneID',    index=['Days_Admitted_Bucket'],
         columns = 'PotentialFraud').reset_index()
    grouped.reset_index(drop = True)
    grouped.fillna(0,inplace=True)
    grouped['Total'] = grouped['No'] + grouped['Yes']
    grouped['% Frauds'] = grouped['Yes']*100/grouped['Total']
    grouped.sort_values(by = ['% Frauds'],inplace=True, ascending = True)
    axis = sns.barplot(x = 'Days_Admitted_Bucket',
            y = '% Frauds',
            data = grouped)
    axis.set(xlabel='Number of Days Admitted', ylabel='% Frauds')
    plt.savefig('FraudDetection/static/images/days_admitted_visualization.jpg')

def third_visualization(inpatient_final_df):
    """
    Creates a visualization for the trend observed in Diagnosis Group Code.
    Args:
        inpatient_final_df : Dataframe have preprocessed data.
    """
    grouped = pd.pivot_table(inpatient_final_df.groupby(
    ['PotentialFraud','DiagnosisGroupCode'])['BeneID'].count().
    reset_index(), values = 'BeneID', index=['DiagnosisGroupCode'],
        columns = 'PotentialFraud').reset_index()
    grouped.reset_index(drop = True)
    grouped.fillna(0,inplace=True)
    grouped['Total'] = grouped['No'] + grouped['Yes']
    grouped['% Frauds'] = grouped['Yes']*100/grouped['Total']
    grouped.sort_values(by = ['% Frauds'],inplace=True, ascending = False)
    top_five_df = grouped.loc[grouped['Total'] > 50].head(5)
    bottom_five_df = grouped.loc[grouped['Total'] > 50].tail(5)
    grouped = pd.concat([bottom_five_df,top_five_df])
    grouped.sort_values(by = ['% Frauds'],inplace=True, ascending = True)
    axis = sns.barplot(x = 'DiagnosisGroupCode',
            y = '% Frauds',
            data = grouped)
    axis.set(xlabel='Diagnosis Group Code', ylabel='% Frauds')
    plt.savefig('FraudDetection/static/images/DiagnosisGroupCode.jpg')


def fourth_visualization(inpatient_final_df):
    """
    Creates a visualization for the trend observed in Claim Amount reimbursed.
    Args:
        inpatient_final_df : Dataframe have preprocessed data.
    """
    grouped = pd.pivot_table(inpatient_final_df.groupby(
          ['PotentialFraud','InscClaimAmtReimbursed_Bucket'])['BeneID'].count().
          reset_index(), values = 'BeneID', index=['InscClaimAmtReimbursed_Bucket'],
          columns = 'PotentialFraud').reset_index()
    grouped.reset_index(drop = True)
    grouped.fillna(0,inplace=True)
    grouped['Total'] = grouped['No'] + grouped['Yes']
    grouped['% Frauds'] = grouped['Yes']*100/grouped['Total']
    grouped.sort_values(by = ['% Frauds'],inplace=True, ascending = True)
    grouped.loc[grouped['Total'] > 20].head(50)
    axis = sns.barplot(x = 'InscClaimAmtReimbursed_Bucket',
            y = '% Frauds',
            data = grouped)
    axis.set(xlabel='Insurance Claim Amount Reimbursed', ylabel='% Frauds')
    plt.savefig('FraudDetection/static/images/Amount_Reimbursed.jpg')
JSON_FILES = './FraudDetection/script/json'

if __name__ == '__main__':

    UPLOAD_DIR = './FraudDetection/script/uploads'
    create_directory_if_not_exists(UPLOAD_DIR)

    app = Flask(__name__, template_folder=os.path.abspath('./FraudDetection/templates'),
                static_folder=os.path.abspath('./FraudDetection/static'))

    app.secret_key = 'my_secret_key'
    app.config['SESSION_TYPE'] = 'filesystem'

    def initialize_app(application):
        """
        Initializes the Flask app with the session object.
        Args:
            application (Flask): The Flask app object to be initialized.
        """
        print("Inside initialize App")
        application.config.from_object(__name__)


    initialize_app(app)

    @app.route('/')
    def home():
        """
        Renders the start page HTML template.
        Returns:
            str: The rendered HTML template.
        """
        state_mapping = pd.read_csv("data/State_Mapping.csv")
        inpatient_final_df = eda(state_mapping)
        first_visualization(inpatient_final_df)
        third_visualization(inpatient_final_df)
        fourth_visualization(inpatient_final_df)
        fig = state_wise_visualization(inpatient_final_df,state_mapping)
        graphjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('start-page.htm',graphJSON=graphjson)

#        print("Inside home")
#        return render_template('start-page.htm')


    @app.route('/home-page')
    def home_page():
        """
        Renders the start page.
        Returns:
            A rendered HTML template.
        """
        print("Inside home page")
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
        if best_model_name == "LODA":
            deployed_model = loda_anomaly_detection
        elif best_model_name == "ECOD":
            deployed_model = ecod_anomaly_detection
        elif best_model_name == "COPOD":
            deployed_model = copod_anomaly_detection
        elif best_model_name == "IFOREST":
            deployed_model = iforest_anomaly_detection
        elif best_model_name == "SUOD":
            deployed_model = suod_anomaly_detection
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


    app.run(debug=True)
