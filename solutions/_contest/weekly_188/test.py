import unittest
import solutions._contest.weekly_188.index as main


class Test(unittest.TestCase):
    def test_buildArray(self):
        test_patterns = [
            ([1, 3], 3, ["Push", "Push", "Pop", "Push"])
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.buildArray(arg1, arg2), expected)

    def test_countTriplets(self):
        test_patterns = [
            ([1, 3, 5, 7, 9], 3),
            ([2, 3, 1, 6, 7], 4),
            ([1, 1, 1, 1, 1], 10),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countTriplets(arg1), expected)


if __name__ == '__main__':
    unittest.main()
