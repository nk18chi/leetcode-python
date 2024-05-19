import unittest
import reverse_integer.index as main


class Test(unittest.TestCase):
    def test_reverse(self):
        test_patterns = [
            (123, 321),
            (-123, -321),
            (1534236469, 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.reverse(arg), expected)


if __name__ == "__main__":
    unittest.main()
