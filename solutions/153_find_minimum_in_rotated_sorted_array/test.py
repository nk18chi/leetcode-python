import unittest
import importlib
f = importlib.import_module(
    'solutions.153_find_minimum_in_rotated_sorted_array.index')


class Test(unittest.TestCase):
    def test_findMin(self):
        test_patterns = [
            ([3, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([3, 4, 5, 1, 2], 1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.findMin(arg), expected)


if __name__ == '__main__':
    unittest.main()
