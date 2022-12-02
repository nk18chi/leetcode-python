import unittest
import solutions.remove_nth_node_from_end_of_list.index as main
from solutions._class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_removeNthFromEnd(self):
        test_patterns = [
            ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
            ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
            ([1], 1, []),
            ([1, 2], 1, [1]),
            ([1, 2], 2, [2]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ln = createListNode(arg1)
                ans: ListNode = getListNode(s.removeNthFromEnd(ln, arg2))
                self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
