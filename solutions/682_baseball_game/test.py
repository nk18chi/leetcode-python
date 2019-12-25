import unittest
import importlib
f = importlib.import_module('solutions.682_baseball_game.index')


class Test(unittest.TestCase):
    def test_calPoints(self):
        test_patterns = [
            (["5", "2", "C", "D", "+"], 30),
            (["5", "-2", "4", "C", "D", "9", "+", "+"], 27)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.calPoints(arg), expected)


if __name__ == '__main__':
    unittest.main()
