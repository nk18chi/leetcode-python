import unittest
import combination_sum.index as main


class Test(unittest.TestCase):
    def test_combinationSum(self):
        test_patterns = [
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2], 1, []),
            ([2, 4, 3, 6], 8, [[2, 2, 2, 2], [2, 2, 4], [4, 4], [2, 3, 3], [2, 6]]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.combinationSum(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
