import unittest


from super_sum_with_tdd import super_sum


class TestSuperSum(unittest.TestCase):
    def test_result_super_sum_1(self):
        self.assertEqual(super_sum(10, 5, 6, 9), 30, msg='Should return 30')

    def test_result_is_int(self):
        result = super_sum([1, 2], 32)
        self.assertNotEqual(result, '35')

    def test_result_super_sum_2(self):
        self.assertEqual(super_sum([10, 5], 5), 20, msg='Should return 20')

    def test_result_exists(self):
        result2 = super_sum(1, 2, 4, 5, 6, 7, 7, 8, [2, 3])
        self.assertTrue(result2)

    def test_result_super_sum_3(self):
        self.assertEqual(super_sum([5, 6], [4, 5], 10),
                         30, msg="should also return 30")

    def test_if_exists_in_list(self):
        result3 = super_sum(1, 4, [3, 5])
        self.assertIn(result3, [13, 9, 7])

    def test_if_string_in_list(self):
        self.assertEqual(super_sum(['', '']), "Your list has non integer items",
                         msg="Should return message-->Your list has non integer items")

    def test_if_string_within_integer_items(self):
        self.assertEqual(super_sum(''), None,
                         msg='Should return \'None')

    def test_result_is_int(self):
        result = super_sum([1, 2], 32)
        self.assertNotEqual(result, '35')
if __name__ == "__main__":
    unittest.main()
