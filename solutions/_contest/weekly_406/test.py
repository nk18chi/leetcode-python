import unittest
import _contest.weekly_406.index as main
from _class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_getSmallestString(self):
        test_patterns = [
            ("45320", "43520"),
            ("001", "001"),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.getSmallestString(arg1),
                    expected,
                )

    def test_modifiedList(self):
        test_patterns = [
            ([1, 2, 3], [1, 2, 3, 4, 5], [4, 5]),
            ([1], [1, 2, 1, 2, 1, 2], [2, 2, 2]),
            ([5], [1, 2, 3, 4], [1, 2, 3, 4]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ln = createListNode(arg2)
                ans: ListNode = getListNode(s.modifiedList(arg1, ln))
                self.assertEqual(ans, expected)

    def test_minimumCost(self):
        test_patterns = [
            (3, 2, [1, 3], [5], 13),
            (2, 2, [7], [4], 15),
            (6, 3, [2, 3, 2, 3, 1], [1, 2], 28),
        ]
        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumCost(arg1, arg2, arg3, arg4), expected)


if __name__ == "__main__":
    unittest.main()
