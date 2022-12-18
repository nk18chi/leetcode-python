# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store

from typing import List, Dict, Tuple


class Solution:
    # Space complexity: O(N)
    class TimeMap:
        def __init__(self):
            self.dict: Dict[str, List[Tuple(str, int)]] = {}

        # Time complexity: O(1)
        def set(self, key: str, value: str, timestamp: int) -> None:
            if key not in self.dict:
                self.dict[key] = []
            self.dict[key].append((value, timestamp))

        # Time complexity: O(logN)
        def get(self, key: str, timestamp: int) -> str:
            if key not in self.dict or len(self.dict[key]) == 0:
                return ""
            arr: List[Tuple[str, int]] = self.dict[key]
            if timestamp < arr[0][1]:
                return ""
            left: int = 0
            right: int = len(arr) - 1
            while left < right:
                mid: int = (right + left) // 2 + 1
                if arr[mid][1] == timestamp:
                    left = mid
                    right = mid
                elif arr[mid][1] < timestamp:
                    left = mid
                else:
                    right = mid - 1
            return arr[left][0]
