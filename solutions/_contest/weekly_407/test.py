import unittest
import _contest.weekly_407.index as main


class Test(unittest.TestCase):
    def test_minChanges(self):
        test_patterns = [(13, 4, 2), (21, 21, 0), (14, 13, -1)]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.minChanges(arg1, arg2),
                    expected,
                )

    def test_doesAliceWin(self):
        test_patterns = [("leetcoder", True), ("bbcd", False)]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.doesAliceWin(arg1),
                    expected,
                )

    def test_maxOperations(self):
        test_patterns = [("1001101", 4), ("00111", 0)]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.maxOperations(arg1),
                    expected,
                )

    def test_minimumOperations(self):
        test_patterns = [([3, 5, 1, 2], [4, 6, 2, 4], 2), ([1, 3, 2], [2, 1, 4], 5)]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.minimumOperations(arg1, arg2),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
