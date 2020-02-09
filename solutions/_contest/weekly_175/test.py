import unittest
import solutions._contest.weekly_175.index as main


class Test(unittest.TestCase):
    def test_checkIfExist(self):
        test_patterns = [
            ([0, 0], True),
            ([-2, 0, 10, -19, 4, 6, -8], False),
            ([-8, -2, 11, 12, 17], False),
            ([4, -7, 11, 4, 18], False),
            ([-16, -13, 8], False),
            ([10, 2, 5, 3], True),
            ([7, 1, 14, 11], True),
            ([3, 1, 7, 11], False)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.checkIfExist(arg), expected)

    def test_minSteps(self):
        test_patterns = [
            ("bab", "aba", 1),
            ("leetcode", "practice", 5),
            ("anagram", "mangaar", 0),
            ("xxyyzz", "xxyyzz", 0)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minSteps(arg1, arg2), expected)

    def test_tweetCounts(self):
        t = main.Solution().TweetCounts()
        t.recordTweet("tweet3", 0)
        t.recordTweet("tweet3", 60)
        t.recordTweet("tweet3", 10)
        t.recordTweet("tweet3", 120)
        print(t.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))
        print(t.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))
        print(t.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))

        # t.recordTweet("tweet3", 0)
        # t.recordTweet("tweet3", 60)
        # t.recordTweet("tweet3", 10)
        # t.recordTweet("tweet3", 120)
        # print(t.getTweetCountsPerFrequency("hour", "tweet3", 0, 210))


if __name__ == '__main__':
    unittest.main()
