import unittest
import ugly_number_2.index as main


class Test(unittest.TestCase):
    def test_nthUglyNumber(self):
        test_patterns = [
            (10, 12),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.nthUglyNumber(arg), expected)


if __name__ == "__main__":
    unittest.main()
