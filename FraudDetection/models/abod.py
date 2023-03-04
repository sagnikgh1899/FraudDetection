import pandas as pd
from pyod.models.abod import ABOD


def abod_anomaly_detection(data, contamination=0.055):
    """
    Detect outliers using Angle-based Outlier Detection (ABOD) algorithm.

    Parameters:
    -----------
    data: pandas.DataFrame
        The data to be processed. Each row represents an observation, and each column represents a feature.
    contamination: float, optional (default=0.1)
        The proportion of outliers in the data set.

    Returns:
    --------
    pandas.Series
        A binary vector with 'True' for outliers and 'False' for inliers.

    """
    # Initialize the ABOD model
    abod = ABOD(contamination=contamination)

    # Fit the model and predict outliers
    y_pred = abod.fit_predict(data)

    # Return a binary vector with 'True' for outliers and 'False' for inliers
    return pd.Series(y_pred == 1, index=data.index)
