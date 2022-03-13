import unittest
import solutions._contest.weekly_283.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_cellsInRange(self):
        test_patterns = [
            ("K1:L2", ["K1", "K2", "L1", "L2"]),
            ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.cellsInRange(arg1), expected)

    def test_minimalKSum(self):
        test_patterns = [
            ([96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84], 35, 794),
            ([1, 2, 8], 7, 44),
            ([1, 2, 11], 10, 77),
            ([5, 6], 6, 25),
            ([1, 4, 25, 10, 25], 2, 5),
            ([53, 41, 90, 33, 84, 26, 50, 32, 63, 47, 66, 43, 29, 88, 71, 28, 83], 76, 3444),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimalKSum(arg1, arg2), expected)

    # def test_createBinaryTree(self):
    #     test_patterns = [
    #         ([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]], [50, 20, 80, 15, 17, 19]),
    #         ([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]], [50, 20, 80, 15, 17, 19]), ([[39, 70, 1], [13, 39, 1], [
    #             85, 74, 1], [74, 13, 1], [38, 82, 1], [82, 85, 1]], [38, 82, None, 85, None, 74, None, 13, None, 39, None, 70]), ]

    #     for i, (arg1, arg2) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = main.Solution()
    #             expected: TreeNode = createTreeNode(arg2)
    #             self.assertEqual(s.createBinaryTree(arg1), expected)

    def test_replaceNonCoprimes(self):
        test_patterns = [
            ([6, 4, 3, 2, 7, 6, 2], [12, 7, 6]),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.replaceNonCoprimes(arg1), expected)


if __name__ == '__main__':
    unittest.main()
