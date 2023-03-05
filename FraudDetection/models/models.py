"""
This module contains the implementation of all the fraud detection models.
ABOD: Angle-based Outlier Detection Algorithm
COPOD: Copula-Based Outlier Detection Algorithm
ECOD: Empirical Cumulative Outlier Detection Algorithm
KNN: K-Nearest Neighbors Algorithm
LOF: Local Outlier Factor Algorithm
"""
import pandas as pd
# pylint: disable=C0413
from pyod.models.abod import ABOD
from pyod.models.copod import COPOD
from pyod.models.ecod import ECOD
from pyod.models.knn import KNN
from pyod.models.lof import LOF


def abod_anomaly_detection(data, contamination=0.055):
    """
    Args:
        data : Pandas DataFrame containing the data for fraud detection.
        contamination : The proportion of outliers in the data set
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    """
    abod = ABOD(contamination=contamination)
    y_pred = abod.fit_predict(data)
    return pd.Series(y_pred == 1, index=data.index)


def copod_anomaly_detection(data, contamination=0.055):
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


def ecod_anomaly_detection(data, contamination=0.055):
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


def knn_anomaly_detection(data, n_neighbors=10, contamination=0.055):
    """
    Args:
        data : Pandas DataFrame containing the data for fraud detection.
        n_neighbors : Number of neighbors to consider for fraud detection.
        contamination : The proportion of outliers in the data set
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    """
    knn = KNN(n_neighbors=n_neighbors, contamination=contamination)
    y_pred = knn.fit_predict(data)
    return pd.Series(y_pred == 1, index=data.index)


def lof_anomaly_detection(data, contamination=0.055):
    """
    Args:
        data : Pandas DataFrame containing the data for fraud detection.
        contamination : The proportion of outliers in the data set
    Returns:
        pandas.Series: A binary vector with 'True' for outliers and 'False' for inliers.
    """
    lof = LOF(contamination=contamination)
    y_pred = lof.fit_predict(data)
    return pd.Series(y_pred == 1, index=data.index)
