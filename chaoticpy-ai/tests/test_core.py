# chaoticpy/tests/test_core.py
import unittest
from chaoticpy.core.chaotic_numbers import ChaoticNumber
from chaoticpy.core.operations import order_chaos
from chaoticpy.utils.helper_functions import calculate_mean

class TestChaoticNumbers(unittest.TestCase):
    def test_addition(self):
        # Test addition operation for chaotic numbers
        num1 = ChaoticNumber(2, 3)
        num2 = ChaoticNumber(4, 5)
        result = num1.add(num2)
        self.assertEqual(result.real, 6)
        self.assertEqual(result.imaginary, 8)

    def test_multiplication(self):
        # Test multiplication operation for chaotic numbers
        num1 = ChaoticNumber(2, 3)
        num2 = ChaoticNumber(4, 5)
        result = num1.multiply(num2)
        self.assertEqual(result.real, -7)
        self.assertEqual(result.imaginary, 22)

class TestOperations(unittest.TestCase):
    def test_order_chaos(self):
        # Test ordering function for chaos set
        chaos_set = [...]  # Replace [...] with an actual chaotic set
        ordered_set = order_chaos(chaos_set)
        self.assertEqual(ordered_set, [...])  # Replace [...] with the expected ordered set

class TestHelperFunctions(unittest.TestCase):
    def test_calculate_mean(self):
        # Test calculation of mean for chaotic set
        chaos_set = [...]  # Replace [...] with an actual chaotic set
        mean = calculate_mean(chaos_set)
        self.assertAlmostEqual(mean, expected_mean, delta=0.001)  # Set the expected mean value and delta

if __name__ == '__main__':
    unittest.main()
