"""
Implements the models for fraud detection
Functions:
    copod_anomaly_detection: Uses the COPOD model
    ecod_anomaly_detection: Uses the ECOD model
    iforest_anomaly_detection: Uses the ECOD model
    loda_anomaly_detection: Uses the ECOD model
    suod_anomaly_detection: Uses the ECOD model
"""
# pylint: disable=E0401
from .models import loda_anomaly_detection
from .models import ecod_anomaly_detection
from .models import copod_anomaly_detection
from .models import iforest_anomaly_detection
from .models import suod_anomaly_detection
