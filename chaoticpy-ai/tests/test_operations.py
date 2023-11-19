# chaoticpy/tests/test_operations.py
import unittest
from chaoticpy.core.operations import order_chaos

class TestOperations(unittest.TestCase):
    def test_order_chaos(self):
        # Test ordering function for a chaos set
        chaos_set = [10, 5, 7, 13, 1]  # Replace with your own chaos set
        ordered_set = order_chaos(chaos_set)
        expected_ordered_set = [1, 5, 7, 10, 13]  # Replace with your expected ordered set
        self.assertEqual(ordered_set, expected_ordered_set)
