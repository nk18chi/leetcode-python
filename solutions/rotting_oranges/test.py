import unittest
import rotting_oranges.index as main


class Test(unittest.TestCase):
    def test_orangesRotting(self):
        test_patterns = [
            ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
            ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
            ([[0, 2]], 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.orangesRotting(arg), expected)


if __name__ == "__main__":
    unittest.main()
