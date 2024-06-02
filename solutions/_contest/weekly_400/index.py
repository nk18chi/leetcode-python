from typing import List, Dict
from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        for i in range(len(nums2)):
            nums2[i] *= k
        result: int = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % nums2[j] == 0:
                    result += 1
        return result

    def compressedString(self, word: str) -> str:
        result: str = ""
        count: int = 0
        for i in range(len(word)):
            count += 1
            if i != len(word) - 1 and word[i] == word[i + 1]:
                if count == 9:
                    result += str(count) + word[i]
                    count = 0
            else:
                result += str(count) + word[i]
                count = 0
        return result

    def numberOfPairs2(self, nums1: List[int], nums2: List[int], k: int) -> int:
        duplicate: Dict[int, int] = {}
        for n in nums2:
            duplicate[n * k] = duplicate.get(n * k, 0) + 1
        counter: Dict[int, int] = {}
        result: int = 0
        nums1_max: int = max(nums1)
        for key, value in duplicate.items():
            for n in range(key, nums1_max + 1, key):
                counter[n] = counter.get(n, 0) + value
        for n in nums1:
            result += counter.get(n, 0)
        return result
