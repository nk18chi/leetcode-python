from typing import List, Set, Dict


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        countMap: Dict[int, int] = {}
        for a in arr:
            countMap[a] = countMap.get(a, 0) + 1
        sortedArr = sorted(countMap.items(), key=lambda x: x[1], reverse=True)
        while k > 0:
            if sortedArr[-1][1] <= k:
                k -= sortedArr[-1][1]
                sortedArr.pop()
            else:
                k -= sortedArr[-1][1]
        return len(sortedArr)

    def minDays(self, A, m, k):
        if m * k > len(A):
            return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m:
                        break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left

    # def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    #     if m == 0:
    #         return 0
    #     if len(bloomDay) < m * k:
    #         return -1
    #     res = float("inf")
    #     count = 0
    #     for i in range(0, len(bloomDay) - m * k + 1):
    #         count = max(bloomDay[i:k + i])
    #         count = max(count, self.minDays(bloomDay[k + i:], m - 1, k))
    #         res = min(res, count)
    #     return res
