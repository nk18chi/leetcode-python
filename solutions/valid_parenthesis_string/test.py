import unittest
import valid_parenthesis_string.index as main


class Test(unittest.TestCase):
    def test_checkValidString(self):
        test_patterns = [
            ("((*)", True),
            ("(((***", True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.checkValidString(arg), expected)


if __name__ == "__main__":
    unittest.main()
