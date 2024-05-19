import unittest
import reverse_string.index as main


class Test(unittest.TestCase):
    def test_reverseString(self):
        test_patterns = [(["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"])]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                s.reverseString(arg)
                self.assertEqual(arg, expected)


if __name__ == "__main__":
    unittest.main()
