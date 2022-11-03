import unittest
import solutions.excel_sheet_column_number.index as main


class Test(unittest.TestCase):
    def test_titleToNumber(self):
        test_patterns = [
            ("A", 1),
            ("AB", 28),
            ("ZY", 701),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.titleToNumber(arg), expected)


if __name__ == '__main__':
    unittest.main()
