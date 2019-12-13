import unittest
import importlib
f = importlib.import_module(
    'solutions.1071_greatest_common_divisor_of_strings.index')


class Test(unittest.TestCase):
    def test_gcdOfStrings(self):
        test_patterns = [
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", ""),
            ("TAUXXTAUXXTAUXXTAUXXTAUXX",
             "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.gcdOfStrings(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
