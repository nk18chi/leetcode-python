from typing import List


class Search:
    def linearSearch(self, arr: List[int], target) -> int:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def binarySearch(self, arr: List[int], start, end, target) -> int:
        if start > end:
            return - 1

        mid: int = (start + end) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            return self.binarySearch(arr, mid + 1, end, target)
        else:
            return self.binarySearch(arr, start, mid - 1, target)
