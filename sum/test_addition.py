import unittest
from addition import my_sum


class TestSumFunction(unittest.TestCase):
    def test_sum1(self):
        """Test sum of Numbers passed to be 10 for 4 and 6"""
        self.assertEqual(my_sum(4, 6), 10)
        """Test the function does not return a None value"""

    def test_sum2(self):
        self.assertIsNotNone(my_sum(1, 2))

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(my_sum(-10, -20), -30)

    def test_decimal_numbers(self):
        """Test negative numbers"""
        self.assertEqual(my_sum(1.4, 2.4), 3.8)

    def test_for_no_arguments(self):
        """Test no arguments passed"""
        self.assertIsNotNone(my_sum(2, 5), msg="No arguments passed")

    def test_not_numbers(self):
        """Test to make sure the number is an integer"""
        result = my_sum('', '')
        self.assertNotEqual(type(result), int, msg='This is not an integer')


if __name__ == "__main__":
    unittest.main()
