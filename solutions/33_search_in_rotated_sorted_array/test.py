import unittest
import importlib
f = importlib.import_module(
    'solutions.33_search_in_rotated_sorted_array.index')


class Test(unittest.TestCase):
    def test_search(self):
        test_patterns = [
            ([7, 8, 1, 2, 3, 4, 5, 6], 2, 3),
            ([4, 5, 6, 7, 0, 1, 2], 6, 2),
            ([5, 1, 3], 5, 0),
            ([3, 5, 1], 5, 1),
            ([1, 3, 5], 4, -1),
            ([1, 3, 5], 1, 0),
            ([2, 1], 2, 0),
            ([1, 2], 3, -1),
            ([1], 0, -1),
            ([], 5, -1),
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.search(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
