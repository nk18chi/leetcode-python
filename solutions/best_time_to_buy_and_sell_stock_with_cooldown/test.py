import unittest
import solutions.best_time_to_buy_and_sell_stock_with_cooldown.index as main


class Test(unittest.TestCase):
    def test_maxProfit(self):
        test_patterns = [
            ([1, 2, 3, 0, 2], 3),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxProfit(arg), expected)


if __name__ == '__main__':
    unittest.main()
