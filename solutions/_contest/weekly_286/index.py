from typing import List, Set
import math


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first: Set[int] = set(nums1)
        duplicated: Set[int] = set()
        for n in nums2:
            if n in first:
                duplicated.add(n)
        res: List[List[int]] = [[], []]
        for n in list(set(nums1)):
            if n not in duplicated:
                res[0].append(n)
        for n in list(set(nums2)):
            if n not in duplicated:
                res[1].append(n)
        return res

    def minDeletion(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        i = 0
        while i < length - 1:
            if (i - count) % 2 == 0 and nums[i] == nums[i + 1]:
                count += 1
            i += 1
        if (length - count) % 2 != 0:
            count += 1
        return count

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res: List[int] = []
        for q in queries:
            if 10 ** (math.ceil(intLength / 2) - 1) * 9 < q:
                res.append(-1)
                continue
            num: str = ""
            numStr = str(q - 1)
            numStr = "0" * (math.ceil(intLength / 2) - len(numStr)) + numStr
            for i in range(len(numStr)):
                n = int(numStr[i])
                if i == 0:
                    n += 1
                num += str(n)
            if intLength % 2 == 0:
                num = num + num[::-1]
            else:
                num = num + num[:-1][::-1]
            res.append(int(num))
        return res
