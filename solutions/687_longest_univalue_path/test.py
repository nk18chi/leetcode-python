import unittest
import importlib
f = importlib.import_module('solutions.687_longest_univalue_path.index')


class Test(unittest.TestCase):
    def test_longestUnivaluePath(self):
        test_patterns = [
            ([5, 4, 5, 1, 1, 5, 3], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                tree = f.createTreeNode(arg)
                self.assertEqual(s.longestUnivaluePath(tree), expected)


if __name__ == '__main__':
    unittest.main()
