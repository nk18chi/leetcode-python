import unittest
import solutions._contest.weekly_289.index as main


class Test(unittest.TestCase):
    def test_digitSum(self):
        test_patterns = [
            ("1234", 2, "37"),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.digitSum(arg1, arg2), expected)

    def test_minimumRounds(self):
        test_patterns = [
            ([2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4),
            ([2, 3, 3], -1),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumRounds(arg1), expected)

    # def test_maxTrailingZeros(self):
    #     test_patterns = [
    #         ([[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]], 3),
    #     ]
    #     for i, (arg1, expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = main.Solution()
    #             self.assertEqual(s.maxTrailingZeros(arg1), expected)


if __name__ == '__main__':
    unittest.main()
