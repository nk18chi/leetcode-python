# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List, Dict


class Solution:
    # Time complexity: O(4 ^ N)
    # Space complexity: O(1)
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phoneMap: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(self, digits: str, path: str):
            if len(digits) == 0:
                return self.res.append(path)
            for n in phoneMap[digits[0]]:
                dfs(self, digits[1:], path + n)

        self.res: List[str] = []
        dfs(self, digits, "")
        return self.res
