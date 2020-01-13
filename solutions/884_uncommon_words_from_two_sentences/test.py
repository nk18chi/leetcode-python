import unittest
import importlib
f = importlib.import_module(
    'solutions.884_uncommon_words_from_two_sentences.index')


class Test(unittest.TestCase):
    def test_uncommonFromSentences(self):
        test_patterns = [
            ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.uncommonFromSentences(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
