import unittest
import importlib
f = importlib.import_module('solutions.746_min_cost_climbing_stairs.index')


class Test(unittest.TestCase):
    def test_minCostClimbingStairs(self):
        test_patterns = [
            ([1, 0, 2, 2], 2),
            ([10, 15, 20], 15),
            ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.minCostClimbingStairs(arg), expected)


if __name__ == '__main__':
    unittest.main()
