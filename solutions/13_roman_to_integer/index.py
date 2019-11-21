# 13. Roman to Integer - Easy
# https://leetcode.com/problems/roman-to-integer/

# from typing import List


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
