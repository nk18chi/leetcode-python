import unittest
import solutions.reverse_words_in_a_string.index as main


class Test(unittest.TestCase):
    def test_reverseWords(self):
        test_patterns = [
            ("the sky is blue", "blue is sky the"),
            ("  hello world!  ", "world! hello"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.reverseWords(arg), expected)


if __name__ == '__main__':
    unittest.main()
