import unittest
import generate_parentheses.index as main


class Test(unittest.TestCase):
    def test_generateParenthesis(self):
        test_patterns = [
            (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.generateParenthesis(arg), expected)


if __name__ == "__main__":
    unittest.main()
