"""
Implements the models for fraud detection
Functions:
    lof_anomaly_detection: Uses the LOF model
    knn_anomaly_detection: Uses the KNN model
    copod_anomaly_detection: Uses the COPOD model
    abod_anomaly_detection: Uses the ABOD model
    ecod_anomaly_detection: Uses the ECOD model
"""
# pylint: disable=E0401
from .models import lof_anomaly_detection
from .models import knn_anomaly_detection
from .models import copod_anomaly_detection
from .models import abod_anomaly_detection
from .models import ecod_anomaly_detection
