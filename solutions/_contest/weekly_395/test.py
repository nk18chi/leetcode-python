import unittest
import solutions._contest.weekly_395.index as main


class Test(unittest.TestCase):
    def test_addedInteger(self):
        test_patterns = [
            ([2, 6, 4], [9, 7, 5], 3),
            ([10], [5], -5),
            ([1, 1, 1, 1], [1, 1, 1, 1], 0),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.addedInteger(arg1, arg2), expected)

    def test_minimumAddedInteger(self):
        test_patterns = [
            ([4, 20, 16, 12, 8], [14, 18, 10], -2),
            ([3, 5, 5, 3], [7, 7], 2),
            ([1, 2, 3, 4, 4, 5, 6, 9, 10], [1, 2, 3, 5, 6, 9, 10], 0),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumAddedInteger(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
