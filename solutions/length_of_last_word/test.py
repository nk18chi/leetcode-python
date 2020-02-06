import unittest

import solutions.length_of_last_word.index as main


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
                s = main.Solution()
                self.assertEqual(s.lengthOfLastWord(arg), expected)


if __name__ == '__main__':
    unittest.main()
