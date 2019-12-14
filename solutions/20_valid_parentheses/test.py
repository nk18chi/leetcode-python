import unittest
import importlib
f = importlib.import_module('solutions.20_valid_parentheses.index')


class Test(unittest.TestCase):
    def test_isValid(self):
        test_patterns = [
            ("[]]", False),
            ("[([]])", False),
            ("{[]}", True),
            ("()", True),
            ("", True),
            ("(a)", False),
            ("()[]{}", True),
            ("(]", False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.isValid(arg), expected)


if __name__ == '__main__':
    unittest.main()
