import unittest
import _contest.weekly_187.index as main


class Test(unittest.TestCase):
    def test_kLengthApart(self):
        test_patterns = [
            ([1, 0, 0, 1, 0, 1], 2, False),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.kLengthApart(arg1, arg2), expected)

    def test_longestSubarray(self):
        test_patterns = [
            ([10, 1, 2, 4, 7, 2], 5, 4),
            ([4, 8, 5, 1, 7, 9], 6, 3),
            ([8], 10, 1),
            # ([24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39], 87, 30),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestSubarray(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
