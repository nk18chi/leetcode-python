import unittest
import solutions.remove_k_digits.index as main


class Test(unittest.TestCase):
    def test_removeKdigits(self):
        test_patterns = [
            ("10", 2, "0"),
            ("1234567890", 9, "0"),
            ("10200", 1, "200"),
            ("1432219", 3, "1219"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.removeKdigits(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
