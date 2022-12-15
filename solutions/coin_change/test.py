import unittest
import solutions.coin_change.index as main


class Test(unittest.TestCase):
    def test_coinChange(self):
        test_patterns = [
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
            ([1], 0, 0)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.coinChange(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
