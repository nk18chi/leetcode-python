import unittest
import odd_even_linked_list.index as main
from _class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_oddEvenList(self):
        test_patterns = [
            ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ln = createListNode(arg)
                ans: ListNode = getListNode(s.oddEvenList(ln))
                self.assertEqual(ans, expected)


if __name__ == "__main__":
    unittest.main()
