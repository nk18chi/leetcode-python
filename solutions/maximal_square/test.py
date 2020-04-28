import unittest
import solutions.maximal_square.index as main


class Test(unittest.TestCase):
    def test_maximalSquare(self):
        test_patterns = [
            ([["1", "0", "1", "0"], ["1", "0", "1", "1"], ["1", "0", "1", "1"], ["1", "1", "1", "1"]], 4),
            ([], 0),
            ([["1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]], 9),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maximalSquare(arg), expected)


if __name__ == '__main__':
    unittest.main()
