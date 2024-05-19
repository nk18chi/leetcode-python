import unittest
import fair_candy_swap.index as main


class Test(unittest.TestCase):
    def test_fairCandySwap(self):
        test_patterns = [
            ([1, 1], [2, 2], [1, 2]),
            ([1, 2, 5], [2, 4], [5, 4]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.fairCandySwap(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
