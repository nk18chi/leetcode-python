import unittest

import split_a_string_in_balanced_strings.index as main


class Test(unittest.TestCase):
    def test_balancedStringSplit(self):
        test_patterns = [("RLRRLLRLRL", 4), ("RLRRRLLRLL", 2)]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.balancedStringSplit(arg), expected)


if __name__ == "__main__":
    unittest.main()
