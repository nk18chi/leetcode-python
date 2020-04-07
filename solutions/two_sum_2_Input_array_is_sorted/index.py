# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    # Two pointer
    # Time complexity: O(n), Space complecity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []

    # # Two pointer(Binary Search)
    # # Time complexity: O(nlogn), Space complecity: O(1)
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i in range(len(numbers)):
    #         left: int = i + 1
    #         right: int = len(numbers) - 1
    #         t: int = target - numbers[i]
    #         while left <= right:
    #             mid: int = (left + right) // 2
    #             if numbers[mid] == t:
    #                 return [i + 1, mid + 1]
    #             if numbers[mid] < t:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return []
