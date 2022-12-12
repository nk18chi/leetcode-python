# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

from typing import List

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]


class Solution:
    def merge(
            self,
            nums1: List[int],
            m: int,
            nums2: List[int],
            n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = sorted(nums1[:m] + nums2[:n])
        for i, a in enumerate(ans):
            nums1[i] = a


if __name__ == "__main__":
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
