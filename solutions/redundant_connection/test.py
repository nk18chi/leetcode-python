import unittest
import solutions.redundant_connection.index as main


class Test(unittest.TestCase):
    def test_findRedundantConnection(self):
        test_patterns = [
            ([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]], [1, 3]),
            ([[1, 5], [3, 4], [3, 5], [4, 5], [2, 4]], [4, 5]),
            ([[1, 2], [1, 3], [2, 3]], [2, 3]),
            ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
            ([[1, 2], [3, 4], [1, 4], [2, 3], [1, 5]], [2, 3]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findRedundantConnection(arg), expected)


if __name__ == '__main__':
    unittest.main()
