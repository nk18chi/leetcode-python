import unittest
import solutions.arranging_coins.index as main


class Test(unittest.TestCase):
    def test_arrangeCoins(self):
        test_patterns = [
            (2, 1),
            (0, 0),
            (6, 3),
            (8, 3),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.arrangeCoins(arg), expected)


if __name__ == '__main__':
    unittest.main()
