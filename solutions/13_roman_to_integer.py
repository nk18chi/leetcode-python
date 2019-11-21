# 13. Roman to Integer - Easy
# https://leetcode.com/problems/roman-to-integer/

# from typing import List
import unittest


def main():
    unittest.main()


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
                s = Solution()
                # tree = createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.romanToInt(arg), expected)


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # # first solution
        # lengh = len(s)
        # if lengh == 0:
        #     return 0

        # sum = 0
        # compare = 0
        # for i in range(0, len(s)):
        #     if s[i] in dict.keys():
        #         if compare == 0:
        #             compare = dict[s[i]]
        #         elif dict[s[i]] <= compare:
        #             sum += compare
        #         else:
        #             sum -= compare

        #         compare = dict[s[i]]

        # sum += compare

        # return sum

        # second solution
        length = len(s)
        if length == 0:
            return 0

        sum = 0
        compare = 0
        for char in s[::-1]:
            if char in dict.keys():
                sum += dict[char] if compare <= dict[char] else - dict[char]
                compare = dict[char]

        return sum


if __name__ == '__main__':
    main()
