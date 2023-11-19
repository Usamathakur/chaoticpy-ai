# chaoticpy/tests/test_utils.py
import unittest
from chaoticpy.utils.helper_functions import calculate_mean

class TestUtils(unittest.TestCase):
    def test_calculate_mean(self):
        # Test calculation of mean for a chaotic set
        chaotic_set = [3, 5, 8, 11, 15]  # Replace with your own chaotic set
        mean = calculate_mean(chaotic_set)
        expected_mean = 8.4  # Replace with your expected mean value
        self.assertAlmostEqual(mean, expected_mean, delta=0.001)  # Adjust delta as needed
