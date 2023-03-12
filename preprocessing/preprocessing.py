"""
Module to perform data preprocesssing. This will be first level preprocessing. For visualization
and machine learning modeling seperate preprocessing will be required according to the requirements.

imports: pandas
"""
import pandas as pd


def read_data():
    """
    function to read csv file
    parameters: None
    return: data frames fraud, beneficiary, inpatient, outpatient.
    raise FileExistsError: raises an exception when file is not found
    """
    try:
        merged = pd.read_csv("data/merged.csv")
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


def save_csv(dataframe):
    """
    function to save preprocessed data into a csv file, to be used for further
    computations of the project.
    parameters: merged dataset
    return: None
    """
    dataframe.to_csv('data/preprocessed.csv', index=False)


def pre_processing():
    """
    function to read and then preprocess data
    parameters: merged dataset
    return: modified dataframe with added WhetherDead column
    """
    dataframe = read_data()
    dataframe = encoding_potential_fraud(dataframe)
    dataframe = encoding_catagorical_data(dataframe)
    dataframe = add_admit_column(dataframe)
    dataframe = add_age_column(dataframe)
    dataframe = adding_dead_column(dataframe)
    return dataframe


def main():
    """
    main function
    parameters: None
    return: None
    """
    dataframe = pre_processing()
    save_csv(dataframe)


if __name__ == "__main__":
    main()
