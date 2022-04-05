import unittest
import solutions._contest.weekly_286.index as main


class Test(unittest.TestCase):
    def test_minDeletion(self):
        test_patterns = [
            ([0, 1, 5, 4, 2, 4, 7, 2, 3, 0, 3, 0, 0, 9, 7, 5, 9, 4, 3, 9, 9, 2,
              1, 6, 3, 1, 0, 7, 6, 6, 6, 0, 1, 7, 1, 9, 4, 9, 3, 3, 4, 5, 0, 3, 8, 7, 1, 8, 4, 5], 4),
            ([1, 1, 2, 3, 5], 1),
            ([1, 1, 2, 2, 3, 3], 2),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minDeletion(arg1), expected)

    def test_kthPalindrome(self):
        test_patterns = [
            ([90], 3, [999]),
            ([1, 2, 3, 4, 5, 90], 3, [101, 111, 121, 131, 141, 999]),
            ([1, 90, 164, 999], 4, [1001, 9999, -1, -1]),
            ([1, 90, 164], 5, [10001, 18981, 26362]),
            ([2, 4, 6], 4, [1111, 1331, 1551]),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.kthPalindrome(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
