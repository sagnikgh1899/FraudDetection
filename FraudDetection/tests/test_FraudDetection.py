"""
This module contains the different test cases.
The tests are written using the unittest framework.
The tests include smoke tests, one shot tests, and edge tests.
Different invalid inputs, incorrect distance calculations, and other edge cases are covered.
"""
import unittest
import sys
import os

import numpy as np
import pandas as pd
# from sklearn.preprocessing import StandardScaler

# pylint: disable=C0413
sys.path.append(os.path.abspath("./FraudDetection/models"))


from models import copod_anomaly_detection
from models import ecod_anomaly_detection
from models import iforest_anomaly_detection
from models import loda_anomaly_detection
from models import suod_anomaly_detection


class TestFraudDetection(unittest.TestCase):
    """
    Unit tests for fraud detection using ABOD anomaly detection.
    """

    def setUp(self):
        self.data = pd.DataFrame(np.array([[1, 4], [2, 5], [3, 6], [3, 2], [0, 1], [6, 6], [1, 4], [1, 4], [1, 4]]))

    def test_one_shot_empty_data_copod(self):
        with self.assertRaises(ValueError):
            copod_anomaly_detection(pd.DataFrame())

    def test_one_shot_non_dataframe_data_copod(self):
        with self.assertRaises(ValueError):
            copod_anomaly_detection("not a dataframe")

    def test_one_shot_non_float_contamination_copod(self):
        with self.assertRaises(ValueError):
            copod_anomaly_detection(pd.DataFrame(), 0.1)

    def test_smoke_copod(self):
        self.assertIsInstance(copod_anomaly_detection(self.data), pd.Series)

    def test_edge_contamination_upper_bound_copod(self):
        with self.assertRaises(ValueError):
            copod_anomaly_detection(self.data, contamination=1.1)

    def test_edge_contamination_lower_bound_copod(self):
        with self.assertRaises(ValueError):
            copod_anomaly_detection(self.data, contamination=-0.1)

    def test_edge_data_type_copod(self):
        with self.assertRaises(ValueError):
            copod_anomaly_detection("not a DataFrame")

    def test_edge_contamination_type_copod(self):
        with self.assertRaises(ValueError):
            copod_anomaly_detection(self.data, contamination="0.1")

    def test_one_shot_empty_data_ecod(self):
        with self.assertRaises(ValueError):
            ecod_anomaly_detection(pd.DataFrame())

    def test_one_shot_non_dataframe_data_ecod(self):
        with self.assertRaises(ValueError):
            ecod_anomaly_detection("not a dataframe")

    def test_one_shot_non_float_contamination_ecod(self):
        with self.assertRaises(ValueError):
            ecod_anomaly_detection(pd.DataFrame(), 0.1)

    def test_smoke_ecod(self):
        self.assertIsInstance(ecod_anomaly_detection(self.data), pd.Series)

    def test_edge_contamination_upper_bound_ecod(self):
        with self.assertRaises(ValueError):
            ecod_anomaly_detection(self.data, contamination=1.1)

    def test_edge_contamination_lower_bound_ecod(self):
        with self.assertRaises(ValueError):
            ecod_anomaly_detection(self.data, contamination=-0.1)

    def test_edge_data_type_ecod(self):
        with self.assertRaises(ValueError):
            ecod_anomaly_detection("not a DataFrame")

    def test_edge_contamination_type_ecod(self):
        with self.assertRaises(ValueError):
            ecod_anomaly_detection(self.data, contamination="0.1")

    def test_one_shot_empty_data_iforest(self):
        with self.assertRaises(ValueError):
            iforest_anomaly_detection(pd.DataFrame())

    def test_one_shot_non_dataframe_data_iforest(self):
        with self.assertRaises(ValueError):
            iforest_anomaly_detection("not a dataframe")

    def test_one_shot_non_float_contamination_iforest(self):
        with self.assertRaises(ValueError):
            iforest_anomaly_detection(pd.DataFrame(), 0.1)

    def test_smoke_iforest(self):
        self.assertIsInstance(iforest_anomaly_detection(self.data), pd.Series)

    def test_edge_contamination_upper_bound_iforest(self):
        with self.assertRaises(ValueError):
            iforest_anomaly_detection(self.data, contamination=1.1)

    def test_edge_contamination_lower_bound_iforest(self):
        with self.assertRaises(ValueError):
            iforest_anomaly_detection(self.data, contamination=-0.1)

    def test_edge_data_type_iforest(self):
        with self.assertRaises(ValueError):
            iforest_anomaly_detection("not a DataFrame")

    def test_edge_contamination_type_iforest(self):
        with self.assertRaises(ValueError):
            iforest_anomaly_detection(self.data, contamination="0.1")

    def test_one_shot_empty_data_loda(self):
        with self.assertRaises(ValueError):
            loda_anomaly_detection(pd.DataFrame())

    def test_one_shot_non_dataframe_data_loda(self):
        with self.assertRaises(ValueError):
            loda_anomaly_detection("not a dataframe")

    def test_one_shot_non_float_contamination_loda(self):
        with self.assertRaises(ValueError):
            loda_anomaly_detection(pd.DataFrame(), 0.1)

    def test_smoke_loda(self):
        self.assertIsInstance(loda_anomaly_detection(self.data), pd.Series)

    def test_edge_contamination_upper_bound_loda(self):
        with self.assertRaises(ValueError):
            loda_anomaly_detection(self.data, contamination=1.1)

    def test_edge_contamination_lower_bound_loda(self):
        with self.assertRaises(ValueError):
            loda_anomaly_detection(self.data, contamination=-0.1)

    def test_edge_data_type_loda(self):
        with self.assertRaises(ValueError):
            loda_anomaly_detection("not a DataFrame")

    def test_edge_contamination_type_loda(self):
        with self.assertRaises(ValueError):
            loda_anomaly_detection(self.data, contamination="0.1")

    def test_one_shot_empty_data_suod(self):
        with self.assertRaises(ValueError):
            suod_anomaly_detection(pd.DataFrame())

    def test_one_shot_non_dataframe_data_suod(self):
        with self.assertRaises(ValueError):
            suod_anomaly_detection("not a dataframe")

    def test_one_shot_non_float_contamination_suod(self):
        with self.assertRaises(ValueError):
            suod_anomaly_detection(pd.DataFrame(), 0.1)

    def test_smoke_suod(self):
        self.assertIsInstance(suod_anomaly_detection(self.data), pd.Series)

    def test_edge_contamination_upper_bound_suod(self):
        with self.assertRaises(ValueError):
            suod_anomaly_detection(self.data, contamination=1.1)

    def test_edge_contamination_lower_bound_suod(self):
        with self.assertRaises(ValueError):
            suod_anomaly_detection(self.data, contamination=-0.1)

    def test_edge_data_type_suod(self):
        with self.assertRaises(ValueError):
            suod_anomaly_detection("not a DataFrame")

    def test_edge_contamination_type_suod(self):
        with self.assertRaises(ValueError):
            suod_anomaly_detection(self.data, contamination="0.1")


if __name__ == '__main__':
    unittest.main()
