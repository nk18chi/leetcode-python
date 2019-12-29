import unittest
import importlib
f = importlib.import_module('solutions.1154_day_of_the_year.index')


class Test(unittest.TestCase):
    def test_dayOfYear(self):
        test_patterns = [
            ("1900-03-25", 84),
            ("2019-01-09", 9),
            ("2019-02-10", 41),
            ("2003-03-01", 60),
            ("2004-03-01", 61),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.dayOfYear(arg), expected)


if __name__ == '__main__':
    unittest.main()
