from sklearn.neighbors import LocalOutlierFactor
import pandas as pd


def lof_anomaly_detection(data, contamination):
    """
    Perform LOF anomaly detection on the input data.
    
    Parameters:
    data (pandas.DataFrame): The input data to be analyzed.
    contamination (float): The expected proportion of outliers in the data.
    
    Returns:
    pandas.Series: A boolean series indicating whether each row of the input data is an outlier.
    """
    lof = LocalOutlierFactor(n_neighbors=20, contamination=contamination)
    y_pred = lof.fit_predict(data)
    return pd.Series(y_pred == -1, index=data.index)
