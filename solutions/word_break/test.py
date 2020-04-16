import unittest
import solutions.word_break.index as main


class Test(unittest.TestCase):
    def test_wordBreak(self):
        test_patterns = [
            ("leetcode", ["leet", "code"], True),
            ("a", ["a"], True),
            ("aaab", ["a", "aa", "aaa"], False),
            ("aaaaaaaaaaab", ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], False),
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
            ("cars", ["car", "ca", "rs"], True),
            ("applepenapple", ["apple", "pen"], True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.wordBreak(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
