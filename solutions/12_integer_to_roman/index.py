# 13. Roman to Integer - Easy
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def intToRoman(self, num: int) -> str:
        self.dict = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        return self.getRoman(num)

    def getRoman(self, n):
        if n == 0:
            return ""
        for k, v in self.dict.items():
            if v == n:
                return k
            elif v < n:
                n -= v
                return k + self.getRoman(n)
            elif n < v:
                del self.dict[k]
                return self.getRoman(n)
