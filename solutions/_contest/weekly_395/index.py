from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        result: int = float("inf")
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            count: int = 0
            diff: int = nums2[0] - nums1[i]
            pointer1: int = 0
            pointer2: int = 0
            while pointer1 < len(nums1) and pointer2 < len(nums2):
                if diff != nums2[pointer2] - nums1[pointer1]:
                    count += 1
                else:
                    pointer2 += 1
                pointer1 += 1
                if count > 2:
                    break
            if count <= 2:
                result = min(diff, result)
        return result
