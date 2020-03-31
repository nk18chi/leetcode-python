# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

from typing import List, Set


class Solution:

    def reverseVowels(self, s: str) -> str:
        left: int = 0
        right: int = len(s) - 1
        vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        arr: List[str] = list(s)
        while left < right:
            if not arr[left] in vowels:
                left += 1
                continue
            if not arr[right] in vowels:
                right -= 1
                continue
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return "".join(arr)
