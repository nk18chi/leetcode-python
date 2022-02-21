import unittest
import solutions._contest.weekly_281.index as main
from solutions._class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_countEven(self):
        test_patterns = [
            (4, 2),
            (30, 14),
            (10, 4),
            (11, 5),
            (12, 5),
            (20, 10),
            (21, 10),
            (22, 11),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countEven(arg1), expected)

    def test_mergeNodes(self):
        test_patterns = [
            ([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ln = createListNode(arg)
                ans: ListNode = getListNode(s.mergeNodes(ln))
                self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
