import unittest
import solutions.base_7.index as main


class Test(unittest.TestCase):
    def test_convertToBase7(self):
        test_patterns = [
            (0, "0"),
            (100, "202"),
            (-7, "-10")
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.convertToBase7(arg), expected)


if __name__ == '__main__':
    unittest.main()
