import unittest
import importlib
f = importlib.import_module('solutions.367_valid_perfect_squar.index')


class Test(unittest.TestCase):
    def test_isPerfectSquare(self):
        test_patterns = [
            (1, True),
            (5, False),
            (16, True),
            (14, False)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.isPerfectSquare(arg), expected)


if __name__ == '__main__':
    unittest.main()
