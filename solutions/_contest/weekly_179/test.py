import unittest
import _contest.weekly_179.index as main


class Test(unittest.TestCase):
    def test_generateTheString(self):
        test_patterns = [(4, "aaab"), (5, "aaaaa")]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = main.createTreeNode([5, 5, 5, 1, 1, 5])
                # n = main.createListNode(arg)
                # self.assertEqual(main.getValFromListNode(s.deleteDuplicates(n)), expected)
                self.assertEqual(s.generateTheString(arg), expected)

    def test_numTimesAllBlue(self):
        test_patterns = [
            ([4, 1, 2, 3], 1),
            ([2, 1, 3, 5, 4], 3),
            ([1, 2, 3, 4, 5, 6], 6),
            ([3, 2, 4, 1, 5], 2),
            ([2, 1, 4, 3, 6, 5], 3),
            ([1, 2, 3, 4, 5, 6], 6),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = main.createTreeNode([5, 5, 5, 1, 1, 5])
                # n = main.createListNode(arg)
                # self.assertEqual(main.getValFromListNode(s.deleteDuplicates(n)), expected)
                self.assertEqual(s.numTimesAllBlue(arg), expected)

    def test_numOfMinutes(self):
        test_patterns = [
            (
                15,
                0,
                [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                3,
            ),
            (6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0], 1),
            (7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1], 21),
            (4, 2, [3, 3, -1, 2], [0, 0, 162, 914], 1076),
        ]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numOfMinutes(arg1, arg2, arg3, arg4), expected)

    # def test_frogPosition(self):
    #     test_patterns = [
    #         (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 20, 6, 0.16666666666666666),
    #         (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7, 0.3333333333333333),
    #         (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4, 0.1666666666666666)
    #     ]

    #     for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = main.Solution()
    #             self.assertEqual(s.frogPosition(arg1, arg2, arg3, arg4), expected)


if __name__ == "__main__":
    unittest.main()
