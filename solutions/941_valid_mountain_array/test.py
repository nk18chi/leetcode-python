import unittest
import importlib
f = importlib.import_module('solutions.941_valid_mountain_array.index')


class Test(unittest.TestCase):

    def test_validMountainArray(self):
        test_patterns = [
            ([0, 3, 2, 1], True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.validMountainArray(arg), expected)


if __name__ == '__main__':
    unittest.main()
