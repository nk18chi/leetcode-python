import unittest
import solutions._contest.weekly_174.index as main


class Test(unittest.TestCase):
    def test_kWeakestRows(self):
        test_patterns = [
            ([[1, 1, 0, 0, 0],
              [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1]], 3, [2, 0, 3])
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.kWeakestRows(arg1, arg2), expected)

    def test_minSetSize(self):
        test_patterns = [
            ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
            ([7, 7, 7, 7, 7, 7], 1),
            ([1, 9], 1),
            ([1000, 1000, 3, 7], 1),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minSetSize(arg1), expected)

    def test_maxProduct(self):
        test_patterns = [
            ([1, 2, 3, 4, 5, 6, 7], 192),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree = main.createTreeNode(arg1)
                self.assertEqual(s.maxProduct(tree), expected)


if __name__ == '__main__':
    unittest.main()
