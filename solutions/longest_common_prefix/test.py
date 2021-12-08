import unittest
import solutions.longest_common_prefix.index as main


class Test(unittest.TestCase):
    def test_longestCommonPrefix(self):
        test_patterns = [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            (["ab", "a"], "a"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.longestCommonPrefix(arg), expected)


if __name__ == '__main__':
    unittest.main()
