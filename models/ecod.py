import numpy as np
import pandas as pd
from pyod.models.ecod import ECOD

def ecod_anomaly_detection(data, contamination):
    """
    Fit and predict outliers using the ECOD algorithm in PyOD library.

    Parameters
    ----------
    data : pandas.DataFrame or numpy.ndarray
        The data to be used for outlier detection.

    Returns
    -------
    pandas.Series
        A binary vector with 'True' for outliers and 'False' for inliers.

    """

    # Initialize the ECOD detector
    ecod = ECOD(contamination = contamination)

    # Fit the model and predict outliers
    y_pred = ecod.fit_predict(data)

    # Return a binary vector with 'True' for outliers and 'False' for inliers
    return pd.Series(y_pred == 1, index=data.index)
