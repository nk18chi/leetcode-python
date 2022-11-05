import unittest
import solutions.search_a_2d_matrix.index as main


class Test(unittest.TestCase):
    def test_searchMatrix(self):
        test_patterns = [
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
            ([[1]], 1, False),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.searchMatrix(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
