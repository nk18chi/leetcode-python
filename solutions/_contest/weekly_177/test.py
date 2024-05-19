import unittest
import _contest.weekly_177.index as main


class Test(unittest.TestCase):
    def test_daysBetweenDates(self):
        test_patterns = [
            ("2020-01-15", "2019-12-31", 15),
            ("2019-06-29", "2019-06-30", 1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.daysBetweenDates(arg1, arg2), expected)

    def test_validateBinaryTreeNodes(self):
        test_patterns = [
            (2, [1, 0], [-1, -1], False),
            (4, [1, -1, 3, -1], [2, 3, -1, -1], False),
            (4, [1, -1, 3, -1], [2, -1, -1, -1], True),
            (6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1], False),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.validateBinaryTreeNodes(arg1, arg2, arg3), expected)

    def test_closestDivisors(self):
        test_patterns = [
            (123, [25, 5]),
            (8, [3, 3]),
            (999, [40, 25]),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.closestDivisors(arg1), expected)

    def test_largestMultipleOfThree(self):
        test_patterns = [
            ([9, 8, 6, 8, 6], "966"),
            ([5, 8], ""),
            ([1], ""),
            ([0, 0, 0, 0, 0, 0], "0"),
            ([8, 6, 7, 1, 0], "8760"),
            ([8, 1, 9], "981"),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.largestMultipleOfThree(arg1), expected)


if __name__ == "__main__":
    unittest.main()
