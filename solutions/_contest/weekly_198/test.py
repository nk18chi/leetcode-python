import unittest
import solutions._contest.weekly_198.index as main


class Test(unittest.TestCase):
    def test_numWaterBottles(self):
        test_patterns = [
            (9, 3, 13),
            (15, 4, 19),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numWaterBottles(arg1, arg2), expected)

    def test_countSubTrees(self):
        test_patterns = [
            (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd", [2, 1, 1, 1, 1, 1, 1]),
            (4, [[0, 2], [0, 3], [1, 2]], "aeed", [1, 1, 2, 1]),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countSubTrees(arg1, arg2, arg3), expected)


if __name__ == '__main__':
    unittest.main()
