import unittest
import solutions.island_perimeter.index as main


class Test(unittest.TestCase):
    def test_islandPerimeter(self):
        test_patterns = [
            ([[0, 1, 1]], 6),
            ([[0, 1, 0, 0],
              [1, 1, 1, 0],
              [0, 1, 0, 0],
              [1, 1, 0, 0]], 16),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.islandPerimeter(arg), expected)


if __name__ == '__main__':
    unittest.main()
