

def encoding_potential_fraud(dataframe):
    dataframe['PotentialFraud'] = dataframe['PotentialFraud'].map({'Yes': 1, 'No': 0})
    corr_to_target = dataframe.corr()['PotentialFraud'].abs().sort_values(ascending=False)