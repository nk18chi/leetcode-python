import unittest
import solutions._contest.weekly_285.index as main


class Test(unittest.TestCase):
    def test_countHillValley(self):
        test_patterns = [
            ([2, 4, 1, 1, 6, 5], 3),
            ([6, 6, 5, 5, 4, 1], 0)
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countHillValley(arg1), expected)

    def test_countCollisions(self):
        test_patterns = [
            ("RRL", 3),
            ("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR", 20),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countCollisions(arg1), expected)

    def test_maximumBobPoints(self):
        test_patterns = [
            (9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0], [0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1]),

        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maximumBobPoints(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
