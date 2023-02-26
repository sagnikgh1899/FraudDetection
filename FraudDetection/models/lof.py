"""
This script implements the LOF (Local Outlier Factor) using PyOD library to detect anomalies.
LOF is an unsupervised outlier detection method which computes the local density deviation of a given data point
with respect to its neighbors. It considers as outliers the samples that have a substantially lower density than
their neighbors.
"""

import numpy as np
import pandas as pd
from pyod.models.lof import LOF


def lof_anomaly_detection(data, contamination):
    """
    Detects anomalies in the input data using the LOF algorithm.

    Parameters:
        data (pandas.DataFrame or numpy.ndarray): Input data to be analyzed.
        contamination (float): Proportion of outliers in the data.

    Returns:
        numpy.ndarray: A boolean array indicating whether each data point is an outlier or not.

    """

    # Initialize LOF model
    lof = LOF(contamination=contamination)

    # Fit the model and predict outliers
    y_pred = lof.fit_predict(data)

    # Return a binary vector with 'True' for outliers and 'False' for inliers
    return pd.Series(y_pred == 1, index=data.index)
