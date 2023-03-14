"""
Module to perform data preprocesssing. This will be first level preprocessing. For visualization
and machine learning modeling seperate preprocessing will be required according to the requirements.

imports: pandas
"""

# pylint: disable=W0612:
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split


def read_data():
    """
    function to read csv file
    parameters: None
    return: data frames fraud, beneficiary, inpatient, outpatient.
    raise FileExistsError: raises an exception when file is not found
    """
    try:
        merged = pd.read_csv("./FraudDetection/data/merged.csv")
    except FileExistsError as error:
        raise error
    return merged


def encoding_potential_fraud(dataframe):
    """
    function encode catagorical field having yes/no into a numerical field
    parameters: merged dataset
    return: modified dataframe with potencialfraud encoded into numerical value
    """
    dataframe['PotentialFraud'] = dataframe['PotentialFraud'].map({'Yes': 1, 'No': 0})
    # corr_to_target = dataframe.corr()['PotentialFraud'].abs().sort_values(ascending=False)
    return dataframe


def encoding_catagorical_data(dataframe):
    """
    function encode catagorical field having yes/no into a numerical field
    parameters: merged dataset
    return: modified dataframe with catagorical columns encoded into numerical value
    """
    dataframe = dataframe.replace({'ChronicCond_Alzheimer': 2,
                                   'ChronicCond_Heartfailure': 2,
                                   'ChronicCond_KidneyDisease': 2,
                                   'ChronicCond_Cancer': 2,
                                   'ChronicCond_ObstrPulmonary': 2,
                                   'ChronicCond_Depression': 2,
                                   'ChronicCond_Diabetes': 2,
                                   'ChronicCond_IschemicHeart': 2,
                                   'ChronicCond_Osteoporasis': 2,
                                   'ChronicCond_rheumatoidarthritis': 2,
                                   'ChronicCond_stroke': 2}, 0)

    dataframe = dataframe.replace({'RenalDiseaseIndicator': 'Y'}, 1)

    dataframe = dataframe.replace(
        {'ChronicCond_Alzheimer': 2, 'ChronicCond_Heartfailure': 2, 'ChronicCond_KidneyDisease': 2,
         'ChronicCond_Cancer': 2, 'ChronicCond_ObstrPulmonary': 2, 'ChronicCond_Depression': 2,
         'ChronicCond_Diabetes': 2, 'ChronicCond_IschemicHeart': 2, 'ChronicCond_Osteoporasis': 2,
         'ChronicCond_rheumatoidarthritis': 2, 'ChronicCond_stroke': 2}, 0)

    dataframe = dataframe.replace({'RenalDiseaseIndicator': 'Y'}, 1)

    return dataframe


def add_admit_column(dataframe):
    """
    function to add a column admitdays
    parameters: merged dataset
    return: modified dataframe with added admitfordays column
    """
    dataframe['AdmissionDt'] = pd.to_datetime(dataframe['AdmissionDt'], format='%Y-%m-%d')
    dataframe['DischargeDt'] = pd.to_datetime(dataframe['DischargeDt'], format='%Y-%m-%d')
    dataframe['AdmitForDays'] = ((dataframe['DischargeDt'] - dataframe['AdmissionDt']).dt.days) + 1
    return dataframe


def add_age_column(dataframe):
    """
    function to add a column age based on DOB and DOD
    parameters: merged dataset
    return: modified dataframe with added age column
    """
    dataframe['DOB'] = pd.to_datetime(dataframe['DOB'], format='%Y-%m-%d')
    dataframe['DOD'] = pd.to_datetime(dataframe['DOD'], format='%Y-%m-%d', errors='ignore')
    dataframe['Age'] = round(((dataframe['DOD'] - dataframe['DOB']).dt.days) / 365)
    dataframe.Age.fillna(round(((pd.to_datetime('2009-12-01', format='%Y-%m-%d') -
                                 dataframe['DOB']).dt.days) / 365),
                         inplace=True)

    dataframe.Age.fillna(round(((pd.to_datetime('2009-12-01', format='%Y-%m-%d') -
                                 dataframe['DOB']).dt.days) / 365),
                         inplace=True)
    return dataframe


def adding_dead_column(dataframe):
    """
    function to add a column to get if the person is dead or not
    parameters: merged dataset
    return: modified dataframe with added WhetherDead column
    """
    dataframe.loc[dataframe.DOD.isna(), 'WhetherDead'] = 0
    dataframe.loc[dataframe.DOD.notna(), 'WhetherDead'] = 1
    dataframe.loc[:, 'WhetherDead'].head(7)
    return dataframe


def create_columns_visualization(dataframe,state_mapping):
    """
    function to add a column to get if the person is dead or not
    parameters: merged dataset
    return: modified dataframe with added WhetherDead column
    """
    inpatient_final_df = dataframe.loc[dataframe['is_Inpatient'] ==1]
    #inpatient_final_df = dataframe
    #inpatient_final_df['DischargeDt'] = inpatient_final_df['DischargeDt'].apply(
    #    lambda x: datetime.strptime(x, '%Y-%m-%d'))
    #inpatient_final_df['AdmissionDt'] = inpatient_final_df['AdmissionDt'].apply(
    #    lambda x: datetime.strptime(x, '%Y-%m-%d'))
    inpatient_final_df['ClaimStartDt'] = inpatient_final_df['ClaimStartDt'].apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d'))
    inpatient_final_df['ClaimEndDt'] = inpatient_final_df['ClaimEndDt'].apply(
        lambda x: datetime.strptime(x, '%Y-%m-%d'))
    #inpatient_final_df['Day_admitted'] = (inpatient_final_df['DischargeDt']-
    #inpatient_final_df['AdmissionDt'])
    #inpatient_final_df['Day_admitted'] = inpatient_final_df['Day_admitted'].apply(
    #    lambda x: x.days)
    inpatient_final_df['Age'] = inpatient_final_df['DOB'].apply(
     lambda x: datetime.strptime("2013-03-03", '%Y-%m-%d').year - x.year)
    inpatient_final_df = inpatient_final_df.merge(state_mapping, on ='State', how = 'left')
    inpatient_final_df.loc[(inpatient_final_df['AdmitForDays'] <= 20),
         "Days_Admitted_Bucket"] = "0-20 Days"
    inpatient_final_df.loc[((inpatient_final_df['AdmitForDays'] > 20)),
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


def save_csv(dataframe):
    """
    function to save preprocessed data into a csv file, to be used for further
    computations of the project.
    parameters: merged dataset
    return: None
    """
    dataframe.to_csv('./FraudDetection/data/preprocessed.csv', index=False)


def save_test_data(x_test,y_test):
    """
    function to save test data into a csv file, to be used for further
    computations of the project.
    parameters: merged dataset
    return: None
    """
    x_test.to_csv('./FraudDetection/data/test.csv', index=False)
    y_test.to_csv('./FraudDetection/data/test_labels.csv', index=False)


def pre_processing():
    """
    function to read and then preprocess data
    parameters: merged dataset
    return: modified dataframe with added WhetherDead column
    """
    dataframe = read_data()
    dataframe = encoding_catagorical_data(dataframe)
    dataframe = add_admit_column(dataframe)
    dataframe = add_age_column(dataframe)
    dataframe = adding_dead_column(dataframe)
    dataframe = encoding_potential_fraud(dataframe)
    return dataframe


def main():
    """
    main function
    parameters: None
    return: None
    """
    dataframe = pre_processing()
    save_csv(dataframe)
    state_mapping = pd.read_csv("./FraudDetection/data/State_Mapping.csv")
    visualization_dataframe = create_columns_visualization(dataframe,state_mapping)
    visualization_dataframe.to_csv('./FraudDetection/data/visualization.csv', index=False)
    #subset =  dataframe.loc[dataframe['is_Inpatient'] == 1][0:20000]
    #outpatient = dataframe.loc[dataframe['is_Inpatient'] == 0][0:38000]
    #subset = pd.concat([subset,outpatient])
    features = dataframe.loc[:, dataframe.columns != "PotentialFraud"]
    labels = dataframe['PotentialFraud']
    x_train, x_test,y_train, y_test = train_test_split(features,labels,
                                   random_state=1,
                                   test_size=0.10,
                                   shuffle=True)
    training_data = pd.concat([x_train,y_train], axis = 1)
    #training_data.to_pickle('./FraudDetection/data/training_data.pkl')
    training_data = training_data.select_dtypes(exclude=['object'])
    training_data = training_data.select_dtypes(exclude=['datetime64[ns]'])
    # Replace NA cols
    training_data.fillna(0,inplace=True)
    # training_data['DeductibleAmtPaid'] = x_train['DeductibleAmtPaid'].fillna(0)
    # training_data.dropna(axis=1, inplace=True)
    training_data.to_csv('./FraudDetection/data/training_data.csv', index=False)
    #training_data.to_pickle('./FraudDetection/data/training_data.pkl')
    x_test = x_test.select_dtypes(exclude=['object'])
    x_test = x_test.select_dtypes(exclude=['datetime64[ns]'])
    # Replace and Drop NA cols
    x_test.fillna(0,inplace=True)
    # x_test['DeductibleAmtPaid'] = x_test['DeductibleAmtPaid'].fillna(0)
    # x_test.dropna(axis=1, inplace=True)
    save_test_data(x_test,y_test)


if __name__ == "__main__":
    main()
