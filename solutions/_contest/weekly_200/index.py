from typing import List, Set, Dict, Tuple, Deque
from collections import deque, defaultdict
from solutions._class.tree_node import TreeNode


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res: int = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, len(arr)):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res

    def getWinner(self, arr: List[int], k: int) -> int:
        curMax: int = max(arr[0], arr[1])
        count: int = 1
        if k == 1:
            return curMax
        for n in arr[2:]:
            if curMax < n:
                curMax = n
                count = 1
            else:
                count += 1
                if count == k:
                    break

        return curMax

    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def count(arr):
            ans = 0
            for i in range(n - 1, -1, -1):
                if arr[i] == 0:
                    ans += 1
                else:
                    break
            return ans

        arr = [count(row) for row in grid]
        ans = 0
        for i in range(n):
            target = n - i - 1
            if arr[i] >= target:
                continue
            flag = False
            for j in range(i + 1, n):
                if arr[j] >= target:
                    flag = True
                    ans += (j - i)
                    arr[i + 1:j + 1] = arr[i:j]
                    break
            if not flag:
                return -1

        return ans
