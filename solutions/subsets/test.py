import unittest
import solutions.subsets.index as main


class Test(unittest.TestCase):
    def test_subsets(self):
        test_patterns = [
            ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.subsets(arg), expected)


if __name__ == '__main__':
    unittest.main()
