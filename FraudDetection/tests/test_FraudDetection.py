# Implementating a pattern test. Use functions in the test.
import unittest
import numpy as np
import sys
import unittest

sys.path.append("../models")
from models import lof_anomaly_detection
from models import knn_anomaly_detection
from models import copod_anomaly_detection
from models import abod_anomaly_detection
from models import ecod_anomaly_detection


class TestEntropy(unittest.TestCase):

    # Smoke test
    def test_entropy_smoke(self):
        if "HELLO" == "HELLO":
            pass
    #     entropy([0.5, 0.2, 0.3])
    #     self.assertTrue(True)
    #
    # # One-shot test
    # def test_certainty(self):
    #     self.assertAlmostEqual(0, entropy([1]))
    #
    # # Pattern test
    # def test_equal_probability(self):
    #     def test(count):
    #         """
    #         Invokes the entropy function for a number of values equal to count
    #         that have the same probability.
    #         :param int count:
    #         """
    #         prob = 1.0 / count
    #         ps = np.repeat(prob, count)
    #         self.assertAlmostEqual(entropy(ps), -np.log2(prob), delta=1e-08,
    #                                msg="Probabilities do not egaul the negative log of the base probability")
    #
    #     for i in range(1, 100):
    #         test(i)
    #
    # # Edge tests
    # def test_invalid_probability_sum(self):
    #     with self.assertRaises(ValueError):
    #         entropy([0.1, 0.5])
    #
    # def test_invalid_probability_individual(self):
    #     with self.assertRaises(ValueError):
    #         entropy([0.6, 1.2, -0.6])


if __name__ == '__main__':
    unittest.main()
