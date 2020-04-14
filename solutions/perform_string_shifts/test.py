import unittest
import solutions.perform_string_shifts.index as main


class Test(unittest.TestCase):
    def test_stringShift(self):
        test_patterns = [
            ("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]], "efgabcd"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.stringShift(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
