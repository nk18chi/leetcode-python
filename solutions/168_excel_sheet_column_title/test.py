import unittest
import importlib
f = importlib.import_module('solutions.168_excel_sheet_column_title.index')


class Test(unittest.TestCase):

    def test_convertToTitle(self):
        test_patterns = [
            (27, "AA"),
            (52, "AZ"),
            (701, "ZY"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.convertToTitle(arg), expected)


if __name__ == '__main__':
    unittest.main()
