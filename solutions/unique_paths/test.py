import unittest

import solutions.unique_paths.index as main


class Test(unittest.TestCase):
    def test_uniquePaths(self):
        test_patterns = [
            (1, 1, 1),
            (7, 3, 28),
            (3, 2, 3),
            (23, 12, 193536720),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.uniquePaths(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
