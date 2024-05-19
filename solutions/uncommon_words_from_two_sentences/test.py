import unittest

import uncommon_words_from_two_sentences.index as main


class Test(unittest.TestCase):
    def test_uncommonFromSentences(self):
        test_patterns = [
            ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.uncommonFromSentences(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
