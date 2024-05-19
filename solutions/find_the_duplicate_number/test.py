import unittest
import find_the_duplicate_number.index as main


class Test(unittest.TestCase):
    def test_findDuplicate(self):
        test_patterns = [
            ([1, 2, 3, 4, 5, 6, 7, 3], 3),
            ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9),
            ([3, 1, 3, 4, 2], 3),
            ([1, 3, 4, 2, 2], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findDuplicate(arg), expected)


if __name__ == "__main__":
    unittest.main()
