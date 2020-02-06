import unittest
import solutions.find_winner_on_a_tic_tac_toe_game.index as main


class Test(unittest.TestCase):

    def test_tictactoe(self):
        test_patterns = [
            ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
            ([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], "B"),
            ([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]], "Draw"),
            ([[0, 0], [1, 1]], "Pending"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.tictactoe(arg), expected)


if __name__ == '__main__':
    unittest.main()
