import unittest

import house_robber.index as main


class Test(unittest.TestCase):
    def test_rob(self):
        test_patterns = [
            ([1, 3, 1, 3, 100], 103),
            ([1, 2, 3, 1, 2, 7, 9, 3, 1, 10, 11], 27),
            ([2, 7, 9, 3, 1], 12),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.rob(arg), expected)


if __name__ == "__main__":
    unittest.main()
