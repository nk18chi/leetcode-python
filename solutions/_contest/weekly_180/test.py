import unittest
import solutions._contest.weekly_180.index as main


class Test(unittest.TestCase):
    def test_luckyNumbers(self):
        test_patterns = [
            ([[3, 7, 8], [9, 11, 13], [15, 16, 17]], [15]),
            ([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]], [12]),
            ([[7, 8], [1, 2]], [7])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = main.createTreeNode([5, 5, 5, 1, 1, 5])
                # n = main.createListNode(arg)
                # self.assertEqual(main.getValFromListNode(s.deleteDuplicates(n)), expected)
                self.assertEqual(s.luckyNumbers(arg), expected)

    # def test_balanceBST(self):
    #     test_patterns = [
    #         ([5, 3, 7, 2, 4, 6, 8], 1),
    #     ]

    #     for i, (arg, expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = main.Solution()
    #             tree = main.createTreeNode(arg)
    #             # n = main.createListNode(arg)
    #             # self.assertEqual(main.getValFromListNode(s.deleteDuplicates(n)), expected)
    #             self.assertEqual(s.balanceBST(tree), expected)

    def test_maxPerformance(self):
        test_patterns = [
            (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
        ]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxPerformance(arg1, arg2, arg3, arg4), expected)


if __name__ == '__main__':
    unittest.main()
