# 13. Roman to Integer - Easy
# https://leetcode.com/problems/roman-to-integer/

import unittest

import solutions.roman_to_integer.index as main


class Test(unittest.TestCase):

    def test_romanToInt(self):
        test_patterns = [
            ("III", 3),
            ("IV", 4),
            ("IX", 9),
            ("ALVIII", 58),
            ("MCMXCIV", 1994),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.romanToInt(arg), expected)


if __name__ == '__main__':
    unittest.main()
