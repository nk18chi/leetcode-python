import unittest
import solutions._contest.weekly_178.index as main


class Test(unittest.TestCase):
    def test_smallerNumbersThanCurrent(self):
        test_patterns = [
            ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
            ([6, 5, 4, 8], [2, 1, 0, 3]),
            ([7, 7, 7, 7], [0, 0, 0, 0]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.smallerNumbersThanCurrent(arg), expected)

    def test_rankTeams(self):
        test_patterns = [
            (["ABC", "ACB", "ABC", "ACB", "ACB"], "ACB"),
            (["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"], "ABC"),
            (["WXYZ", "XYZW"], "XWYZ"),
            (["ZMNAGUEDSJYLBOPHRQICWFXTVK"], "ZMNAGUEDSJYLBOPHRQICWFXTVK"),
            (["M", "M", "M", "M"], "M"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.rankTeams(arg), expected)


if __name__ == '__main__':
    unittest.main()
