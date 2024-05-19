import unittest
import sqrtx.index as main


class Test(unittest.TestCase):
    def test_mySqrt(self):
        test_patterns = [
            (0, 0),
            (1, 1),
            (2, 1),
            (4, 2),
            (8, 2),
            (16, 4),
            (24, 4),
            (25, 5),
            (1024, 32),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.mySqrt(arg), expected)


if __name__ == "__main__":
    unittest.main()
