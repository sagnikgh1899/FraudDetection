"""
This module contains the implementation of the fraud detection models
LODA: Lightweight On-line Detector of Anomalies
ECOD: Empirical Cumulative Outlier Detection Algorithm
COPOD: Copula-Based Outlier Detection Algorithm
IFOREST: Isolation Forest Algorithm
SUOD: Large-scale Unsupervised Heterogeneous Outlier Detection
"""
import pandas as pd
# pylint: disable=C0413
from pyod.models.loda import LODA
from pyod.models.ecod import ECOD
from pyod.models.copod import COPOD
from pyod.models.iforest import IForest
from pyod.models.suod import SUOD
from sklearn.preprocessing import StandardScaler


def copod_anomaly_detection(data, contamination=0.1):
    """
    Args:
        data : Pandas DataFrame containing the data for fraud detection.
        contamination : The proportion of outliers in the data set
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    Raises:
        TypeError: If the input data is not a Pandas DataFrame
        ValueError: If the input data is empty or the contamination parameter is not between 0 and 1
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a Pandas DataFrame")
    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Input data is empty")
    if not isinstance(contamination, float):
        raise ValueError("Contamination must be a float")
    if not 0 <= contamination <= 1:
        raise ValueError("Contamination must be between 0 and 1")
    copod = COPOD(contamination=contamination)
    y_pred = copod.fit_predict(data)
    return pd.Series(y_pred == 1, index=data.index)


def ecod_anomaly_detection(data, contamination=0.1):
    """
    Args:
        data: Pandas DataFrame containing the data for fraud detection.
        contamination : The proportion of outliers in the data set
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a Pandas DataFrame")
    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Input data is empty")
    if not isinstance(contamination, float):
        raise ValueError("Contamination must be a float")
    if not 0 <= contamination <= 1:
        raise ValueError("Contamination must be between 0 and 1")
    ecod = ECOD(contamination=contamination)
    y_pred = ecod.fit_predict(data)
    return pd.Series(y_pred == 1, index=data.index)


def iforest_anomaly_detection(data, contamination=0.1):
    """
    Args:
        data (pandas.DataFrame): Input data for anomaly detection.
        contamination (float): The proportion of outliers in the data set.
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a Pandas DataFrame")
    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Input data is empty")
    if not isinstance(contamination, float):
        raise ValueError("Contamination must be a float")
    if not 0 <= contamination <= 1:
        raise ValueError("Contamination must be between 0 and 1")
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), index=data.index)
    model = IForest(contamination=contamination)
    model.fit(data_scaled)
    y_pred = model.predict(data_scaled)

    # Create binary vector
    return pd.Series(y_pred == 1, index=data.index)


def loda_anomaly_detection(data, n_bins=10, contamination=0.1):
    """
    Args:
        data (pandas.DataFrame): Input data for anomaly detection.
        n_bins (int): The number of bins to use for the histogram.
        contamination (float): The proportion of outliers in the data set.
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a Pandas DataFrame")
    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Input data is empty")
    if not isinstance(contamination, float):
        raise ValueError("Contamination must be a float")
    if not 0 <= contamination <= 1:
        raise ValueError("Contamination must be between 0 and 1")
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), index=data.index)
    model = LODA(n_bins=n_bins, contamination=contamination)
    model.fit(data_scaled)
    y_pred = model.predict(data_scaled)

    # Create binary vector
    return pd.Series(y_pred == 1, index=data.index)


def suod_anomaly_detection(data, contamination=0.1):
    """
    Args:
        data (pandas.DataFrame): Input data for anomaly detection.
        contamination (float): The proportion of outliers in the data set.
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a Pandas DataFrame")
    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Input data is empty")
    if not isinstance(contamination, float):
        raise ValueError("Contamination must be a float")
    if not 0 <= contamination <= 1:
        raise ValueError("Contamination must be between 0 and 1")
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), index=data.index)
    detector_list = [ECOD(), COPOD(), IForest()]
    model = SUOD(detector_list, n_jobs=2, combination='maximization',
           verbose=False, contamination=contamination)
    model.fit(data_scaled)
    y_pred = model.predict(data_scaled)
    return pd.Series(y_pred == 1, index=data.index)
