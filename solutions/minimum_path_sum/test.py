import unittest
import minimum_path_sum.index as main


class Test(unittest.TestCase):
    def test_minPathSum(self):
        test_patterns = [
            ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minPathSum(arg), expected)


if __name__ == "__main__":
    unittest.main()
