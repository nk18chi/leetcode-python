import unittest
import missing_number.index as main


class Test(unittest.TestCase):
    def test_missingNumber(self):
        test_patterns = [
            ([3, 0, 1], 2),
            ([0, 1], 2),
            ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.missingNumber(arg), expected)


if __name__ == "__main__":
    unittest.main()
