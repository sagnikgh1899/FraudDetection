'''
This script defines a function knn_anomaly_detection that applies kNN (k-Nearest Neighbors) to detect anomalies in the input data.
'''

import numpy as np
import pandas as pd
from pyod.models.knn import KNN


def knn_anomaly_detection(data, n_neighbors=10, contamination=0.055):
    """
    Apply kNN (k-Nearest Neighbors) to detect anomalies in the input data.

    Parameters:
    -----------
    data : pandas.DataFrame
        Input data with shape (n_samples, n_features)
    n_neighbors : int, optional (default=5)
        Number of neighbors to consider for outlier detection.
    contamination : float, optional (default=0.1)
        Proportion of outliers to expect in the data set.

    Returns:
    --------
    pandas.Series
        A binary vector with 'True' for outliers and 'False' for inliers.
    """
    # Initialize the kNN model
    knn = KNN(n_neighbors=n_neighbors, contamination=contamination)

    # Fit the model and predict outliers
    y_pred = knn.fit_predict(data)

    # Return a binary vector with 'True' for outliers and 'False' for inliers
    return pd.Series(y_pred == 1, index=data.index)
