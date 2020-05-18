import unittest
import solutions.find_all_anagrams_in_a_string.index as main


class Test(unittest.TestCase):
    def test_findAnagrams(self):
        test_patterns = [
            ("", "a", []),
            ("abab", "ab", [0, 1, 2]),
            ("cbaebabacd", "abc", [0, 6]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findAnagrams(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
