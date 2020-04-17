import unittest
import solutions.number_of_closed_islands.index as main


class Test(unittest.TestCase):
    def test_closedIsland(self):
        test_patterns = [
            ([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]], 1),
            ([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]], 2),
            ([[1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 0, 1],
              [1, 0, 1, 0, 1, 0, 1],
              [1, 0, 1, 1, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1]], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.closedIsland(arg), expected)


if __name__ == '__main__':
    unittest.main()
