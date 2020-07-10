import unittest
import solutions.three_sum.index as main


class Test(unittest.TestCase):
    def test_threeSum(self):
        test_patterns = [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.threeSum(arg), expected)


if __name__ == '__main__':
    unittest.main()
