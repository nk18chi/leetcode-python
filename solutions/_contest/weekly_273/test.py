import unittest
import solutions._contest.weekly_273.index as main
from solutions._class.tree_node import TreeNode, createTreeNode


class Test(unittest.TestCase):
    def test_isSameAfterReversals(self):
        test_patterns = [
            (526, True),
            (1800, False),
            (0, True)
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isSameAfterReversals(arg1), expected)

    def test_executeInstructions(self):
        test_patterns = [
            (3, [0, 1], "RRDDLU", [1, 5, 4, 3, 1, 0]),
            (2, [1, 1], "LURD", [4, 1, 0, 0]),
            (1, [0, 0], "LRUD", [0, 0, 0, 0])
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.executeInstructions(arg1, arg2, arg3), expected)


if __name__ == '__main__':
    unittest.main()
