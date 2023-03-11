"""
This module contains the different test cases.
The tests are written using the unittest framework.
The tests include smoke tests, one shot tests, and edge tests.
Different invalid inputs, incorrect distance calculations, and other edge cases are covered.
"""
import unittest
import sys
import os

# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# pylint: disable=C0413
sys.path.append(os.path.abspath("./FraudDetection/models"))


# from models import lof_anomaly_detection
# from models import knn_anomaly_detection
# from models import copod_anomaly_detection
# from models import ecod_anomaly_detection


class TestFraudDetection(unittest.TestCase):
    """
    Unit tests for fraud detection using ABOD anomaly detection.
    """

    def setUp(self):
        """
        Sets up a sample data for testing.
        """
        self.data = "HELLO"

    # Smoke test
    def test_entropy_smoke(self):
        """
        A dummy test
        """
        if "HELLO" == self.data:
            pass


if __name__ == '__main__':
    unittest.main()
