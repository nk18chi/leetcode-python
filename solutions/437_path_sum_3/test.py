import unittest
import importlib
f = importlib.import_module('solutions.437_path_sum_3.index')


class Test(unittest.TestCase):
    def test_pathSum(self):
        test_patterns = [
            ([10, 5, -3, 3, 2, 2, 11, 3, -2, 4, 1], 8, 3),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                tree = f.createTreeNode(arg1)
                self.assertEqual(s.pathSum(tree, arg2), expected)


if __name__ == '__main__':
    unittest.main()
