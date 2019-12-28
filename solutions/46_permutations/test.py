import unittest
import importlib
f = importlib.import_module('solutions.46_permutations.index')


class Test(unittest.TestCase):
    def test_permute(self):
        test_patterns = [([1, 2, 3], [[1, 2, 3], [2, 3, 1], [
            3, 1, 2], [1, 3, 2], [2, 1, 3], [3, 2, 1]]), ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.permute(arg), expected)


if __name__ == '__main__':
    unittest.main()
