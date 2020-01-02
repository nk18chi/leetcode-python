import unittest
import importlib
f = importlib.import_module('solutions.538_convert_bst_to_greater_tree.index')


class Test(unittest.TestCase):
    def test_convertBST(self):
        test_patterns = [
            ([5, 2, 13], [18, 20, 13])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                tree = f.createTreeNode(arg)
                # self.assertEqual(s.convertBST(tree), expected)


if __name__ == '__main__':
    unittest.main()
