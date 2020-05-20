import unittest
import solutions.online_stock_span.index as main


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [
            ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ]

        s = main.Solution().StockSpanner()
        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                for j in range(len(arg)):
                    self.assertEqual(s.next(arg[j]), expected[j])


if __name__ == '__main__':
    unittest.main()
