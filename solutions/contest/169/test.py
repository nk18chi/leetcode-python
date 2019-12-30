import unittest
import importlib
f = importlib.import_module('solutions.contest.169.index')


class Test(unittest.TestCase):
    def test_canReach(self):
        test_patterns = [
            ([4, 2, 3, 0, 3, 1, 2], 5, True),
            ([4, 2, 3, 0, 3, 1, 2], 0, True),
            ([3, 0, 2, 1, 2], 2, False)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.canReach(arg1, arg2), expected)

    def test_getAllElements(self):
        test_patterns = [
            ([2, 1, 4], [1, 0, 3], [0, 1, 1, 2, 3, 4]),
            ([0, -10, 10], [5, 1, 7, 0, 2], [-10, 0, 0, 1, 2, 5, 7, 10])
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                tree1 = f.createTreeNode(arg1)
                tree2 = f.createTreeNode(arg2)
                self.assertEqual(s.getAllElements(tree1, tree2), expected)

    def test_sumZero(self):
        test_patterns = [
            (1, [0]),
            (2, [1, -1]),
            (3, [0, 1, -1])
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.sumZero(arg1), expected)


if __name__ == '__main__':
    unittest.main()
