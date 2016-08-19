import unittest

from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_three(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')

    def test_divisible_by_five(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')

    def test_divisible_by_both(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')

    def test_returns_number_if_above_fail(self):
        self.assertEqual(fizz_buzz(29), 29)


if __name__ == "__main__":
    unittest.main()
