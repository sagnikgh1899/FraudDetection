"""
This module contains the implementation of all the fraud detection models
ABOD: Angle-based Outlier Detection Algorithm
COPOD: Copula-Based Outlier Detection Algorithm
ECOD: Empirical Cumulative Outlier Detection Algorithm
KNN: K-Nearest Neighbors Algorithm
LOF: Local Outlier Factor Algorithm
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
    """
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
    # Scale the data
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), index=data.index)

    # Train the IForest model
    model = IForest(contamination=contamination)
    model.fit(data_scaled)

    # Predict the outliers
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
    # Scale the data
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), index=data.index)

    # Train the LODA model
    model = LODA(n_bins=n_bins, contamination=contamination)
    model.fit(data_scaled)

    # Predict the outliers
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
    # Scale the data
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data), index=data.index)

    # Train the LOCI model
    # initialized a group of outlier detectors for acceleration
    detector_list = [ECOD(), COPOD(), IForest()]
    model = SUOD(detector_list, n_jobs=2, combination='maximization',
           verbose=False, contamination=contamination)
    model.fit(data_scaled)

    # Predict the outliers
    y_pred = model.predict(data_scaled)

    # Create binary vector
    return pd.Series(y_pred == 1, index=data.index)
