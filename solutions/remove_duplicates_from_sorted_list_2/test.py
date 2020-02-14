import unittest
import solutions.remove_duplicates_from_sorted_list_2.index as main


class Test(unittest.TestCase):
    def test_deleteDuplicates(self):
        test_patterns = [
            ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
            ([1, 1, 1, 2, 3], [2, 3]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                n = main.createListNode(arg)
                self.assertEqual(main.getValFromListNode(s.deleteDuplicates(n)), expected)


if __name__ == '__main__':
    unittest.main()
