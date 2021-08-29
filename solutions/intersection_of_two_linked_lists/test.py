import unittest
import solutions.intersection_of_two_linked_lists.index as main
from solutions._class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_getIntersectionNode(self):
        test_patterns = [
            ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], [8, 4, 5]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ln1 = createListNode(arg1)
                ln2 = createListNode(arg2)
                print(ln1)
                ans = s.getIntersectionNode(ln1, ln2)
                print(ans)
                self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
