import unittest
import solutions.path_sum_2.index as main


class Test(unittest.TestCase):
    def test_pathSum(self):
        test_patterns = [
            ([5, 4, 8, 11, 20, 13, 4, 7, 2, 30, 32, 5, 1], 22, [[5, 4, 11, 2]]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree = main.createTreeNode(arg1)
                self.assertEqual(s.pathSum(tree, arg2), expected)


if __name__ == '__main__':
    unittest.main()
