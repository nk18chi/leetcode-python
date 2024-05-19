import unittest
import _contest.weekly_182.index as main


class Test(unittest.TestCase):
    def test_findLucky(self):
        test_patterns = [
            ([1, 2, 2, 3, 3, 3], 3),
            ([2, 2, 3, 4], 2),
            ([2, 2, 2, 3, 3], -1),
            ([5], -1),
            ([7, 7, 7, 7, 7, 7, 7], 7),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findLucky(arg), expected)

    def test_numTeams(self):
        test_patterns = [([2, 5, 3, 4, 1], 3), ([2, 1, 3], 0), ([1, 2, 3, 4], 4)]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numTeams(arg), expected)

    def test_UndergroundSystem(self):
        s = main.Solution()
        u = s.UndergroundSystem()
        u.checkIn(45, "Leyton", 3)
        u.checkOut(45, "Waterloo", 15)
        self.assertEqual(12.0, u.getAverageTime("Leyton", "Waterloo"))


if __name__ == "__main__":
    unittest.main()
