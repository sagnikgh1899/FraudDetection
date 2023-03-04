"""
COPOD: COPOD (COunt-based POD) algorithm for outlier detection.

COPOD is a simple yet powerful algorithm that utilizes the count-based approach for outlier detection.

"""

# Import necessary libraries
from pyod.models.copod import COPOD
import pandas as pd


def copod_anomaly_detection(data, contamination=0.055):
    """
    Function to detect outliers in a pandas dataframe using the COPOD algorithm.

    Parameters:
    -----------
    data : pandas dataframe
        Dataframe containing the data for anomaly detection.

    Returns:
    --------
    A pandas Series with 'True' for outliers and 'False' for inliers.
    """

    # Create COPOD object
    lof = COPOD(contamination=contamination)

    # Fit the model and predict outliers
    y_pred = lof.fit_predict(data)

    # Return a binary vector with 'True' for outliers and 'False' for inliers
    return pd.Series(y_pred == 1, index=data.index)
