import unittest

import solutions.valid_perfect_squar.index as main


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
                s = main.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.isPerfectSquare(arg), expected)


if __name__ == '__main__':
    unittest.main()
