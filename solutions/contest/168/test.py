import unittest
import importlib
f = importlib.import_module('solutions.contest.168.index')


class Test(unittest.TestCase):
    def test_isPossibleDivide(self):
        test_patterns = [
            ([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3, True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.isPossibleDivide(arg1, arg2), expected)

    def test_maxFreq(self):
        test_patterns = [
            ("aababcaab", 2, 3, 4, 2),
            ("aaaa", 1, 3, 3, 2),
            ("aabcabcab", 2, 2, 3, 3),
            ("abcde", 2, 3, 3, 0)
        ]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.maxFreq(arg1, arg2, arg3, arg4), expected)

    # def test_maxCandies(self):
    #     test_patterns = [
    #         # ([1, 0, 1, 0], [7, 5, 4, 100], [
    #         #     [], [], [1], []], [[1, 2], [3], [], []], [0], 16),
    #         # ([1, 0, 0, 0, 0, 0],
    #         #     [1, 1, 1, 1, 1, 1],
    #         #     [[1, 2, 3, 4, 5], [], [], [], [], []],
    #         #     [[1, 2, 3, 4, 5], [], [], [], [], []],
    #         #     [0],
    #         #     6
    #         #  ),
    #         ([1, 0, 0, 0],
    #          [1, 2, 3, 4],
    #             [[1, 2], [3], [], []],
    #             [[2], [3], [1], []],
    #             [0], 10)
    #     ]

    #     for i, (arg1, arg2, arg3, arg4, arg5,
    #             expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = f.Solution()
    #             # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
    #             self.assertEqual(
    #                 s.maxCandies(
    #                     arg1,
    #                     arg2,
    #                     arg3,
    #                     arg4,
    #                     arg5),
    #                 expected)


if __name__ == '__main__':
    unittest.main()
