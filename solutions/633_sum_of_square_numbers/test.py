import unittest
import importlib
f = importlib.import_module('solutions.633_sum_of_square_numbers.index')


class Test(unittest.TestCase):
    def test_judgeSquareSum(self):
        test_patterns = [
            (6, False),
            (5, True),
            (3, False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.judgeSquareSum(arg), expected)


if __name__ == '__main__':
    unittest.main()
