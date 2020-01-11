import unittest
import importlib
f = importlib.import_module('solutions.965_univalued_binary_tree.index')


class Test(unittest.TestCase):
    def test_isUnivalTree(self):
        test_patterns = [
            ([1, 2], False),
            ([1, 1, 1, 1, 1, 1, 1], True),
            ([1, 1, 1, 1, 1, 1, 2], False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                tree = f.createTreeNode(arg)
                self.assertEqual(s.isUnivalTree(tree), expected)


if __name__ == '__main__':
    unittest.main()
