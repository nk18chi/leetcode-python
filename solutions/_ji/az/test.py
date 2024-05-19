import unittest
import _contest.weekly_281.index as main
from _class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_maxSubarrayLength(self):
        test_patterns = [
            ([-1, 1, 1, 1], 3),
            ([1, -1, -1, -1, 1, 1], 4),
            ([1, -1, 1, -1], 4),
            ([1, 1, 1, 1], 4),
            ([-1, 1, 1, -1], 4),
            ([-1, -1, 1, -1], 3),
            ([1, 1, 1, -1, 1], 3),
            ([1, 1, 1, -1, 1, -1, -1], 6),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxSubarrayLength(arg1), expected)

    def test_getImbalanceRank(self):
        test_patterns = [
            ([4, 1, 3, 2], 3),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getImbalanceRank(arg1), expected)


if __name__ == "__main__":
    unittest.main()
