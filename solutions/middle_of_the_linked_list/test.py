import unittest
import solutions.middle_of_the_linked_list.index as main
from solutions._class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_middleNode(self):
        test_patterns = [
            ([1, 2, 3, 4, 5], [3, 4, 5]),
            ([1, 2, 3, 4, 5, 6], [4, 5, 6])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ln = createListNode(arg)
                ans: ListNode = getListNode(s.middleNode(ln))
                self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
