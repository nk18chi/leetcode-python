import unittest
import solutions.minimum_indlex_sum_of_two_lists.index as main


class Test(unittest.TestCase):
    def test_findRestaurant(self):
        test_patterns = [
            (["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"], ["Shogun"]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = main.createTreeNode([5, 5, 5, 1, 1, 5])
                # n = main.createListNode(arg)
                # self.assertEqual(main.getValFromListNode(s.deleteDuplicates(n)), expected)
                self.assertEqual(s.findRestaurant(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
