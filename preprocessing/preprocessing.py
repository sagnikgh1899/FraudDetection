"""
Module to perform data preprocesssing
imports: pandas
"""
import pandas as pd



def encoding_potential_fraud(dataframe):
    """
    function encode catagorical field having yes/no into a numerical field
    parameters: merged dataset
    return: modified dataframe with potencialfraud encoded into numerical value
    """
    dataframe['PotentialFraud'] = dataframe['PotentialFraud'].map({'Yes': 1, 'No': 0})
    corr_to_target = dataframe.corr()['PotentialFraud'].abs().sort_values(ascending=False)
    return dataframe

def encoding_catagorical_data(dataframe):
    """
    function encode catagorical field having yes/no into a numerical field
    parameters: merged dataset
    return: modified dataframe with catagorical columns encoded into numerical value
    """
    dataframe = dataframe.replace({'ChronicCond_Alzheimer': 2, 'ChronicCond_Heartfailure': 2, 'ChronicCond_KidneyDisease': 2,
                           'ChronicCond_Cancer': 2, 'ChronicCond_ObstrPulmonary': 2, 'ChronicCond_Depression': 2, 
                           'ChronicCond_Diabetes': 2, 'ChronicCond_IschemicHeart': 2, 'ChronicCond_Osteoporasis': 2, 
                           'ChronicCond_rheumatoidarthritis': 2, 'ChronicCond_stroke': 2 }, 0)

    dataframe = dataframe.replace({'RenalDiseaseIndicator': 'Y'}, 1)

    dataframe = dataframe.replace({'ChronicCond_Alzheimer': 2, 'ChronicCond_Heartfailure': 2, 'ChronicCond_KidneyDisease': 2,
                            'ChronicCond_Cancer': 2, 'ChronicCond_ObstrPulmonary': 2, 'ChronicCond_Depression': 2, 
                            'ChronicCond_Diabetes': 2, 'ChronicCond_IschemicHeart': 2, 'ChronicCond_Osteoporasis': 2, 
                            'ChronicCond_rheumatoidarthritis': 2, 'ChronicCond_stroke': 2 }, 0)

    dataframe = dataframe.replace({'RenalDiseaseIndicator': 'Y'}, 1)

    return dataframe

def add_admit_column(dataframe):
    """
    function to add a column admitdays
    parameters: merged dataset
    return: modified dataframe with added admitfordays column
    """
    dataframe['AdmissionDt'] = pd.to_datetime(dataframe['AdmissionDt'] , format = '%Y-%m-%d')
    dataframe['DischargeDt'] = pd.to_datetime(dataframe['DischargeDt'],format = '%Y-%m-%d')
    dataframe['AdmitForDays'] = ((dataframe['DischargeDt'] - dataframe['AdmissionDt']).dt.days)+1
    return dataframe

def add_age_column(dataframe):
    """
    function to add a column age based on DOB and DOD
    parameters: merged dataset
    return: modified dataframe with added age column
    """
    dataframe['DOB'] = pd.to_datetime(dataframe['DOB'] , format = '%Y-%m-%d')
    dataframe['DOD'] = pd.to_datetime(dataframe['DOD'],format = '%Y-%m-%d',errors='ignore')
    dataframe['Age'] = round(((dataframe['DOD'] - dataframe['DOB']).dt.days)/365)
    dataframe.Age.fillna(round(((pd.to_datetime('2009-12-01' , format = '%Y-%m-%d') - dataframe['DOB']).dt.days)/365),
                                 inplace=True)

    dataframe.Age.fillna(round(((pd.to_datetime('2009-12-01' , format = '%Y-%m-%d') - dataframe['DOB']).dt.days)/365),
                                 inplace=True)
    return dataframe







