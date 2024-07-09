import unittest
import _contest.weekly_405.index as main


class Test(unittest.TestCase):
    def test_getEncryptedString(self):
        test_patterns = [
            ("dart", 3, "tdar"),
            ("aaa", 1, "aaa"),
        ]
        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getEncryptedString(arg1, arg2), expected)

    def test_validStrings(self):
        test_patterns = [
            (3, ["010", "011", "101", "110", "111"]),
            (1, ["0", "1"]),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.validStrings(arg1), expected)

    def test_numberOfSubmatrices(self):
        test_patterns = [
            ([[".", ".", "."], ["Y", "X", "X"], ["X", "Y", "Y"]], 4),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numberOfSubmatrices(arg1), expected)


if __name__ == "__main__":
    unittest.main()
