import unittest

import minimum_absolute_difference.index as main


class Test(unittest.TestCase):
    def test_minimumAbsDifference(self):
        test_patterns = [
            ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minimumAbsDifference(arg), expected)


if __name__ == "__main__":
    unittest.main()
