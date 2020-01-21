import unittest
import importlib
f = importlib.import_module(
    'solutions.594_longest_harmonious_subsequence.index')


class Test(unittest.TestCase):
    def test_findLHS(self):
        test_patterns = [
            ([1, 1, 1, 1], 0),
            ([1, 3, 2, 2, 5, 2, 3, 7], 5),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.findLHS(arg), expected)


if __name__ == '__main__':
    unittest.main()
