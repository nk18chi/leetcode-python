import unittest
import solutions.is_subsequence.index as main


class Test(unittest.TestCase):
    def test_isSubsequence(self):
        test_patterns = [
            ("abc", "ahbgdc", True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isSubsequence(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
