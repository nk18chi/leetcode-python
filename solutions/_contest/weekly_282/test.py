import unittest
import solutions._contest.weekly_282.index as main


class Test(unittest.TestCase):

    def test_prefixCount(self):
        test_patterns = [
            (["pay", "attention", "practice", "attend"], "at", 2),
            (["leetcode", "win", "loops", "success"], "code", 0),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.prefixCount(arg1, arg2), expected)

    def test_minSteps(self):
        test_patterns = [
            ("leetcode", "coats", 7),
            ("night", "thing", 0)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minSteps(arg1, arg2), expected)

    def test_minimumTime(self):
        test_patterns = [
            ([1, 2, 3], 5, 3),
            ([2], 1, 2),
            ([1, 2], 10, 7),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumTime(arg1, arg2), expected)

    def test_minimumFinishTime(self):
        test_patterns = [
            ([[2, 3], [3, 4]], 5, 4, 21),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumFinishTime(arg1, arg2, arg3), expected)


if __name__ == '__main__':
    unittest.main()
