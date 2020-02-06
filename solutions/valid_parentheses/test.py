import unittest

import solutions.valid_parentheses.index as main


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
                s = main.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.isValid(arg), expected)


if __name__ == '__main__':
    unittest.main()
