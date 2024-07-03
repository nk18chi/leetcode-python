import unittest
import _contest.weekly_404.index as main


class Test(unittest.TestCase):
    def test_maxHeightOfTriangle(self):
        test_patterns = [
            (2, 4, 3),
            (10, 10, 5),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxHeightOfTriangle(arg1, arg2), expected)

    def test_maximumLength(self):
        test_patterns = [
            ([2, 39, 23], 2),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maximumLength(arg1), expected)

    def test_maximumLength2(self):
        test_patterns = [
            ([1, 2, 3, 4, 9, 22], 3, 5),
            ([1, 4, 3, 2, 3, 3, 1, 2, 4, 2, 4, 2], 3, 8),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maximumLength2(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
