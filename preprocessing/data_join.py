"""
Module to join data
imports: numpy, pandas
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


def read_data():
    """
    function to read csv files
    parameters: None
    return: None
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
    """

    # Join the files
    merged = pd.merge(beneficiary, inpatient, on='BeneID', how='outer')
    merged = pd.merge(merged, outpatient, on='BeneID', how='outer')
    merged = pd.merge(merged, train, on='Provider', how='left')

    # Save the merged file as a CSV
    merged.to_csv('merged.csv', index=False)

