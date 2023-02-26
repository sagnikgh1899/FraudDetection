"""
Module to perform initial eda on merged dataset from data_join.py to get initial idea about the dataset for preprocessing and further computations.
imports: numpy, pandas
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
        merged=pd.read_csv("../data/merged.csv")
    except FileExistsError as error:
        raise error
    return merged

def explore_data(dataframe):
    """
    function to get number of rows and columns, all columns, to show first 5 data.
    parameters: merged dataset
    return: None    
    """
    print("Number of rows and columns:", dataframe.shape)
    print("\nColumn names:\n", dataframe.columns)
    print("\nFirst 5 rows:\n", dataframe.head())
def missing_data(dataframe):
    """
    function to prints the percentage of missing values in each column.
    parameters: merged dataset
    return: None
    """
    total_missing = dataframe.isnull().sum().sort_values(ascending=False)
    percent_missing = (total_missing / len(dataframe)) * 100
    missing_data = pd.concat([total_missing, percent_missing], axis=1, keys=['Total', 'Percent'])
    print("Percentage of missing values in each column:\n", missing_data)

