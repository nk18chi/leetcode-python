import unittest
import importlib
f = importlib.import_module('solutions.58_length_of_last_word.index')


class Test(unittest.TestCase):
    def test_lengthOfLastWord(self):
        test_patterns = [
            ("Hello Word", 4),
            ("Hello World", 5),
            ("Hello World ", 5),
            (" ", 0),
            ("", 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.lengthOfLastWord(arg), expected)


if __name__ == '__main__':
    unittest.main()
