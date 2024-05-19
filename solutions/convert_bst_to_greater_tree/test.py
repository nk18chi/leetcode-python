import unittest
import convert_bst_to_greater_tree.index as main


class Test(unittest.TestCase):
    def test_convertBST(self):
        test_patterns = [([5, 2, 13], [18, 20, 13])]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree = main.createTreeNode(arg)
                # self.assertEqual(s.convertBST(tree), expected)


if __name__ == "__main__":
    unittest.main()
