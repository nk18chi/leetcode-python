from typing import List, Set, Dict
import bisect


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            isPalindrome: bool = True
            for i in range(len(word) // 2):
                if word[i] != word[i * -1 - 1]:
                    isPalindrome = False
                    break
            if isPalindrome:
                return word
        return ""

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words: List[str] = []
        left: int = 0
        for i in range(len(spaces)):
            right: int = spaces[i]
            words.append(s[left:right])
            left = right
        words.append(s[right:])
        return " ".join(words)

    def getDescentPeriods(self, prices: List[int]) -> int:
        res: int = len(prices)
        cur: int = 0
        for i in range(len(prices) - 1):
            if prices[i] - prices[i + 1] == 1:
                cur += 1
                res += cur
            else:
                cur = 0
        return res

    def kIncreasing(self, arr: List[int], k: int) -> int:
        res: int = len(arr)
        for i in range(k):
            sub: List[int] = []
            for j in range(i, len(arr), k):
                idx = bisect.bisect_right(sub, arr[j])
                if idx == len(sub):
                    sub.append(arr[j])
                else:
                    sub[idx] = arr[j]
            res -= len(sub)
        return res
