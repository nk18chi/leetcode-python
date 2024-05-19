import unittest
import _contest.weekly_173.index as main


class Test(unittest.TestCase):
    def test_removePalindromeSub(self):
        test_patterns = [("ababa", 1), ("abb", 2), ("baabb", 2), ("", 0)]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.removePalindromeSub(arg), expected)

    def test_filterRestaurants(self):
        test_patterns = [
            (
                [
                    [1, 4, 1, 40, 10],
                    [2, 8, 0, 50, 5],
                    [3, 8, 1, 30, 4],
                    [4, 10, 0, 10, 3],
                    [5, 1, 1, 15, 1],
                ],
                0,
                50,
                10,
                [4, 3, 2, 1, 5],
            ),
            (
                [
                    [1, 4, 1, 40, 10],
                    [2, 8, 0, 50, 5],
                    [3, 8, 1, 30, 4],
                    [4, 10, 0, 10, 3],
                    [5, 1, 1, 15, 1],
                ],
                1,
                50,
                10,
                [3, 1, 5],
            ),
        ]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.filterRestaurants(arg1, arg2, arg3, arg4), expected)

    # def test_findTheCity(self):
    #     test_patterns = [
    #         (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3),
    #         (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2, 0),
    #     ]

    #     for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = main.Solution()
    #             self.assertEqual(s.findTheCity(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
