import unittest
import solutions.remove_linked_list_elements.index as main


class Test(unittest.TestCase):
    def test_removeElements(self):
        test_patterns = [
            ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                n1 = main.createListNode(arg1)
                n2 = main.createListNode(expected)
                self.assertEqual(main.getValFromListNode(s.removeElements(n1, arg2)), n2)


if __name__ == '__main__':
    unittest.main()
