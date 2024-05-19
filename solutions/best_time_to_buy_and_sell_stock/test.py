import unittest
import best_time_to_buy_and_sell_stock.index as main


class Test(unittest.TestCase):
    def test_maxProfit(self):
        test_patterns = [
            ([], 0),
            ([1, 2], 1),
            ([2, 1, 2, 1, 0, 1, 2], 2),
            ([7, 6, 4, 3, 1], 0),
            ([7, 1, 5, 3, 6, 4], 5),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxProfit(arg), expected)


if __name__ == "__main__":
    unittest.main()
