import unittest
import solutions.backspace_string_compare.index as main


class Test(unittest.TestCase):
    def test_backspaceCompare(self):
        test_patterns = [
            ("bb#b", "b", False),
            ("ab##", "c#d#", True),
            ("ab#c", "ad#c", True),
            ("a##c", "#a#c", True),
            ("a#c", "b", False),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.backspaceCompare(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
