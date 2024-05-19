import unittest
import power_of_three.index as main


class Test(unittest.TestCase):
    def test_isPowerOfThree(self):
        test_patterns = [
            (27, True),
            (0, False),
            (-1, False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isPowerOfThree(arg), expected)


if __name__ == "__main__":
    unittest.main()
