import unittest
import importlib
f = importlib.import_module('solutions.62_unique_paths.index')


class Test(unittest.TestCase):
    def test_uniquePaths(self):
        test_patterns = [
            # (1, 1, 1),
            # (3, 2, 3),
            # (7, 3, 28),
            (23, 12, 193536720),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.uniquePaths(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
