"""
Module to merge the data into a single dataframe.
Dataset to join: fraud, beneficiary, inpatient, outpatient
to generate,please run function generate_merged_file(), it will automatically generate the merged file in data foler.
imports: numpy, pandas
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


def read_data():
    """
    function to read csv files
    parameters: None
    return: data frames fraud, beneficiary, inpatient, outpatient.
    raise FileExistsError: raises an exception when file is not found
    """
    try:
        fraud=pd.read_csv("../data/Train-1542865627584.csv")
        beneficiary=pd.read_csv("../data/Train_Beneficiarydata-1542865627584.csv")
        inpatient=pd.read_csv("../data/Train_Inpatientdata-1542865627584.csv")
        outpatient=pd.read_csv("../data/Train_Outpatientdata-1542865627584.csv")
    except FileExistsError as error:
        raise error
    return fraud, beneficiary, inpatient, outpatient
    
def join_csv(fraud, beneficiary, inpatient, outpatient):
    """
    function to join csv files. Joining by key BeneID, Provider.
    parameters: fraud, beneficiary, inpatient, outpatient dataframes
    return: merged csv
    """

    # Join the files
    merged = pd.merge(beneficiary, inpatient, on='BeneID', how='outer')
    merged = pd.merge(merged, outpatient, on='BeneID', how='outer')
    merged = pd.merge(merged, train, on='Provider', how='left')

    # Save the merged file as a CSV
    merged.to_csv('../data/merged.csv', index=False)

def generate_merged_file():
    fraud, beneficiary, inpatient, outpatient = read_data()
    join_csv(fraud, beneficiary, inpatient, outpatient)

