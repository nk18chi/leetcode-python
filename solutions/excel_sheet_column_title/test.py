import unittest
import solutions.excel_sheet_column_title.index as main


class Test(unittest.TestCase):

    def test_convertToTitle(self):
        test_patterns = [
            (27, "AA"),
            (52, "AZ"),
            (701, "ZY"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.convertToTitle(arg), expected)


if __name__ == '__main__':
    unittest.main()
