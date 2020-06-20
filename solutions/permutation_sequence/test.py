import unittest
import solutions.permutation_sequence.index as main


class Test(unittest.TestCase):
    def test_getPermutation(self):
        test_patterns = [
            (3, 3, "213"),
            (4, 9, "2314"),
            (3, 2, "132"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getPermutation(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
