import pandas as pd

def initial_eda():
    """
    """
    print('Train Shape:',Train.shape,'\n')
    print('Train Sample:\n',Train.head(2),'\n')

    print('\n Test Shape:',Test.shape,'\n')
    print('Test Sample: \n',Test.head(2))
    print('\n Total missing values in Train :',Train.isna().sum().sum())

    print('\n Total missing values in Train :',Test.isna().sum().sum())