import unittest
import solutions.find_first_and_last_position_of_element_in_sorted_array.index as main


class Test(unittest.TestCase):
    def test_searchRange(self):
        test_patterns = [
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
            ([], 0, [-1, -1]),
            ([1], 1, [0, 0]),
            ([5, 7, 7, 8, 8], 8, [3, 4]),
            ([8, 8, 10], 8, [0, 1]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.searchRange(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
