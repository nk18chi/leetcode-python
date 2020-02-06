import unittest
import solutions.baseball_game.index as main


class Test(unittest.TestCase):
    def test_calPoints(self):
        test_patterns = [
            (["5", "2", "C", "D", "+"], 30),
            (["5", "-2", "4", "C", "D", "9", "+", "+"], 27)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.calPoints(arg), expected)


if __name__ == '__main__':
    unittest.main()
