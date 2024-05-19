import unittest

import largest_time_for_given_digits.index as main


class Test(unittest.TestCase):
    def test_largestTimeFromDigits(self):
        test_patterns = [
            ([2, 0, 6, 6], "06:26"),
            ([1, 2, 3, 4], "23:41"),
            ([5, 5, 5, 5], ""),
            ([0, 0, 0, 0], "00:00"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.largestTimeFromDigits(arg), expected)


if __name__ == "__main__":
    unittest.main()
