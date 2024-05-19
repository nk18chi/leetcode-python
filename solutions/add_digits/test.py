import unittest
import add_digits.index as main


class Test(unittest.TestCase):
    def test_addDigits(self):
        test_patterns = [
            (38, 2),
            (20420, 8),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.addDigits(arg), expected)


if __name__ == "__main__":
    unittest.main()
