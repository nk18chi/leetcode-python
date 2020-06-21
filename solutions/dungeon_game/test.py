import unittest
import solutions.dungeon_game.index as main


class Test(unittest.TestCase):
    def test_calculateMinimumHP(self):
        test_patterns = [
            ([[1, -3, 3], [0, -2, 0], [-3, -3, -3]], 3),
            ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.calculateMinimumHP(arg), expected)


if __name__ == '__main__':
    unittest.main()
