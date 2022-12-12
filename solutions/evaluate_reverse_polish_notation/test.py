import unittest
import solutions.evaluate_reverse_polish_notation.index as main


class Test(unittest.TestCase):
    def test_evalRPN(self):
        test_patterns = [
            (["2", "1", "+", "3", "*"], 9),
            (["4", "13", "5", "/", "+"], 6),
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.evalRPN(arg), expected)


if __name__ == '__main__':
    unittest.main()
