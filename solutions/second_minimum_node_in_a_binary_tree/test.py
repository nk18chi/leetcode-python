import unittest
import second_minimum_node_in_a_binary_tree.index as main


class Test(unittest.TestCase):
    def test_findSecondMinimumValue(self):
        test_patterns = [
            ([1, 1, 3, 1, 1, 3, 4, 3, 1, 2, 1, 3, 8, 4, 8], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree = main.createTreeNode(arg)
                self.assertEqual(s.findSecondMinimumValue(tree), expected)


if __name__ == "__main__":
    unittest.main()
