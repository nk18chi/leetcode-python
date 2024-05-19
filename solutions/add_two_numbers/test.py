import unittest
import add_two_numbers.index as main
from _class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_addTwoNumbers(self):
        test_patterns = [
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                l1 = createListNode(arg1)
                l2 = createListNode(arg2)
                ans: ListNode = getListNode(s.addTwoNumbers(l1, l2))
                self.assertEqual(ans, expected)


if __name__ == "__main__":
    unittest.main()
