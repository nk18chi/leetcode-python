import unittest
import solutions.bitwise_and_of_numbers_range.index as main


class Test(unittest.TestCase):
    def test_rangeBitwiseAnd(self):
        test_patterns = [
            (7, 9, 0),
            (8, 15, 8),
            (12, 15, 12),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.rangeBitwiseAnd(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
