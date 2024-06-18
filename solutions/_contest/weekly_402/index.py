from typing import List, Dict


class Solution:
    def countCompleteDayPairs1(self, hours: List[int]) -> int:
        result: int = 0
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    result += 1
        return result

    def countCompleteDayPairs2(self, hours: List[int]) -> int:
        formatHours: List[int] = []
        for hour in hours:
            formatHours.append(hour % 24)
        result: int = 0
        appear: Dict[int, int] = {}
        for hour in formatHours:
            diff: int = (24 - hour) % 24
            if diff in appear:
                result += appear[diff]
            if hour not in appear:
                appear[hour] = 0
            appear[hour] += 1
        return result

    # original
    # def maximumTotalDamage(self, power: List[int]) -> int:
    #     power.sort()
    #     appear: List[int] = [0]
    #     sumMap: Dict[int, List[int]] = {0: [0, 0]}  # [sum, max]
    #     for p in power:
    #         if p in sumMap:
    #             sumMap[p][0] += p
    #         else:
    #             sumMap[p] = [p, p]
    #             for i in range(len(appear) - 1, -1, -1):
    #                 if i < len(appear) - 3:
    #                     break
    #                 if appear[i] >= p - 2:
    #                     continue
    #                 sumMap[p][0] += sumMap[appear[i]][1]
    #                 break
    #             appear.append(p)
    #         result: int = 0
    #         for i in range(len(appear) - 1, -1, -1):
    #             if i < len(appear) - 3:
    #                 break
    #             result = max(result, sumMap[appear[i]][0])
    #         sumMap[p][1] = result
    #     return result

    # optimized
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        appear: List[int] = [0, 0, 0]
        sumMap: Dict[int, int] = {}
        for p in power:
            if p not in sumMap:
                sumMap[p] = 0
                appear.append(p)
            sumMap[p] += p
        dp = [0] * len(appear)
        for i in range(3, len(appear)):
            if appear[i] - appear[i - 1] > 2:
                dp[i] = dp[i - 1] + sumMap[appear[i]]
            elif appear[i] - appear[i - 2] > 2:
                dp[i] = max(dp[i - 2] + sumMap[appear[i]], dp[i - 1])
            else:
                dp[i] = max(sumMap[appear[i]] + dp[i - 3], dp[i - 1])
        return dp[-1]
