import unittest

import univalued_binary_tree.index as main


class Test(unittest.TestCase):
    def test_isUnivalTree(self):
        test_patterns = [
            ([1, 2], False),
            ([1, 1, 1, 1, 1, 1, 1], True),
            ([1, 1, 1, 1, 1, 1, 2], False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree = main.createTreeNode(arg)
                self.assertEqual(s.isUnivalTree(tree), expected)


if __name__ == "__main__":
    unittest.main()
