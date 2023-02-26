"""
Module to perform initial eda on merged dataset from data_join.py to get initial idea about the dataset for preprocessing and further computations.
imports: numpy, pandas
"""
import pandas as pd

def get_dimention():
    """
    """
    print('Train Shape:',Train.shape,'\n')
    print('Train Sample:\n',Train.head(2),'\n')

    print('\n Test Shape:',Test.shape,'\n')
    print('Test Sample: \n',Test.head(2))
    print('\n Total missing values in Train :',Train.isna().sum().sum())

    print('\n Total missing values in Train :',Test.isna().sum().sum())