import unittest
import _contest.weekly_424.index as main


class Test(unittest.TestCase):
    def test_countValidSelections(self):
        test_patterns = [
            ([1, 0, 2, 0, 3], 2),
            ([2, 3, 4, 0, 4, 1, 0], 0),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.countValidSelections(arg1),
                    expected,
                )

    def test_isZeroArray(self):
        test_patterns = [
            ([1, 0, 1], [[0, 2]], True),
            ([4, 3, 2, 1], [[1, 3], [0, 2]], False),
            ([2, 0, 2, 1, 0, 0], [[0, 5], [0, 3]], True),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.isZeroArray(arg1, arg2),
                    expected,
                )

    def test_minZeroArray(self):
        test_patterns = [
            ([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]], 2),
            ([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]], -1),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(
                    s.minZeroArray(arg1, arg2),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
