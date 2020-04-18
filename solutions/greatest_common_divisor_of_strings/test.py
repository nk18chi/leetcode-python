import unittest

import solutions.greatest_common_divisor_of_strings.index as main


class Test(unittest.TestCase):
    def test_gcdOfStrings(self):
        test_patterns = [
            ("TAUXXTAUXXTAUXXTAUXXTAUXX",
             "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"),
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", ""),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.gcdOfStrings(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
