import unittest

import solutions.permutations.index as main


class Test(unittest.TestCase):
    def test_permute(self):
        test_patterns = [([1, 2, 3], [[1, 2, 3], [2, 3, 1], [
            3, 1, 2], [1, 3, 2], [2, 1, 3], [3, 2, 1]]), ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.permute(arg), expected)


if __name__ == '__main__':
    unittest.main()
