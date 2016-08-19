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

    def test_format_exactly_equal(self):
        self.assertNotEqual(fizz_buzz(6), 'FIZZ')
        self.assertNotEqual(fizz_buzz(25), 'buzz')
        self.assertNotEqual(fizz_buzz(30), 'fizzBuzz')

    def test_result_is_string(self):
        result1 = fizz_buzz(12)
        self.assertIs(result1, str)

    def test_result_for_number_is_int(self):
        self.assertNotEqual(fizz_buzz(17, '17'))

    def test_error_raised(self):
        with self.assertRaises(TypeError):
            fizz_buzz('')

    def test_result_is_returned(self):
        self.assertTrue(fizz_buzz(12))

    def test_returned_value_is_an_integer(self):
        self.assertEqual(type(fizz_buzz(15)), int)


if __name__ == "__main__":
    unittest.main()
