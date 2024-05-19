import unittest

import zigzag_conversion.index as main


class Test(unittest.TestCase):
    def test_convert(self):
        test_patterns = [
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("A", 2, "A"),
            ("ABCD", 2, "ACBD"),
            ("AB", 1, "AB"),
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.convert(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
