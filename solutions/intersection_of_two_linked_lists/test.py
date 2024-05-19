import unittest
import intersection_of_two_linked_lists.index as main
from _class.list_node import createListNode, getListNode


class Test(unittest.TestCase):
    def test_getIntersectionNode(self):
        test_patterns = [
            ([4, 1], [5, 6, 1], [8, 4, 5]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ln1 = createListNode(arg1)
                ln2 = createListNode(arg2)
                ln3 = createListNode(expected)
                p1 = ln1
                p2 = ln2
                while p1.next:
                    p1 = p1.next
                while p2.next:
                    p2 = p2.next
                p1.next = ln3
                p2.next = ln3
                ans = s.getIntersectionNode(ln1, ln2)
                self.assertEqual(getListNode(ans), expected)


if __name__ == "__main__":
    unittest.main()
