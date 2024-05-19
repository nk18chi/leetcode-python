import unittest

import non_decreasing_rray.index as main


class Test(unittest.TestCase):
    def test_checkPossibility(self):
        test_patterns = [
            ([-1, 4, 2, 3], True),
            ([1, 2, 4, 5, 3], True),
            ([2, 3, 3, 2, 4], True),
            ([3, 4, 2, 3], False),
            ([4, 2, 3], True),
            ([3, 2, 3, 2, 4], False),
            ([4, 2, 1], False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.checkPossibility(arg), expected)


if __name__ == "__main__":
    unittest.main()
