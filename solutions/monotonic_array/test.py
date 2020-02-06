import unittest

import solutions.monotonic_array.index as main


class Test(unittest.TestCase):
    def test_isMonotonic(self):
        test_patterns = [
            ([1, 3, 2], False),
            ([1, 2, 2, 3], True),
            ([6, 5, 4, 4], True),
            ([1, 2, 4, 5], True),
            ([1, 1, 1], True),
            ([11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5], False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isMonotonic(arg), expected)


if __name__ == '__main__':
    unittest.main()
