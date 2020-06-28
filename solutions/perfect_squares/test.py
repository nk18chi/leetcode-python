import unittest
import solutions.perfect_squares.index as main


class Test(unittest.TestCase):
    def test_numSquares(self):
        test_patterns = [
            (12, 3),
            (13, 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numSquares(arg), expected)


if __name__ == '__main__':
    unittest.main()
