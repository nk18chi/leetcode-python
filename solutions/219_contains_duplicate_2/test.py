import unittest
import importlib
f = importlib.import_module('solutions.219_contains_duplicate_2.index')


class Test(unittest.TestCase):
    def test_containsNearbyDuplicate(self):
        test_patterns = [
            ([1, 2, 3, 1], 3, True),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1, 2, 3], 2, False)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(
                    s.containsNearbyDuplicate(
                        arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
