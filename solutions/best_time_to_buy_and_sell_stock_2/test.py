import unittest
import best_time_to_buy_and_sell_stock_2.index as main


class Test(unittest.TestCase):
    def test_maxProfit(self):
        test_patterns = [
            ([6, 1, 3, 2, 4, 7], 7),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxProfit(arg), expected)


if __name__ == "__main__":
    unittest.main()
