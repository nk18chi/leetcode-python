import unittest
import _contest.weekly_400.index as main


class Test(unittest.TestCase):
    def test_minimumChairs(self):
        test_patterns = [
            ("EEEEEEE", 7),
            ("ELELEEL", 2),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumChairs(arg1), expected)

    def test_countDays(self):
        test_patterns = [
            (10, [[5, 7], [1, 3], [9, 10]], 2),
            (5, [[2, 4], [1, 3]], 1),
            (6, [[1, 6]], 0),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countDays(arg1, arg2), expected)

    def test_clearStars(self):
        test_patterns = [
            ("d*d*", ""),
            ("aaba*", "aab"),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.clearStars(arg1), expected)


if __name__ == "__main__":
    unittest.main()
