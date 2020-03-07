import unittest
import solutions.word_break.index as main


class Test(unittest.TestCase):
    def test_wordBreak(self):
        test_patterns = [
            ("aaaaaaaaaaab", ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], False),
            ("leetcode", ["leet", "code"], True),
            ("applepenapple", ["apple", "pen"], True),
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], False)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.wordBreak(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
