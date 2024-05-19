import unittest
import longest_duplicate_substring.index as main


class Test(unittest.TestCase):
    def test_longestDupSubstring(self):
        test_patterns = [
            ("banana", "ana"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestDupSubstring(arg), expected)


if __name__ == "__main__":
    unittest.main()
