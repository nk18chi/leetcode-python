from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        dict = {}
        for n in nums:
            dict[n] = dict[n] + 1 if n in dict else 1

        while(dict != {}):
            target = min(dict.keys())
            for i in range(k):
                if target + i in dict:
                    dict[target + i] -= 1
                    if dict[target + i] == 0:
                        del dict[target + i]
                else:
                    return False

        return True

# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
    def maxFreq(
            self,
            s: str,
            maxLetters: int,
            minSize: int,
            maxSize: int) -> int:
        dict = {}
        for num in range(maxSize, minSize - 1, -1):
            for i in range(len(s) - num + 1):
                t = s[i: i + num]
                if len(set(t)) > maxLetters:
                    continue

                dict[t] = dict[t] + 1 if t in dict else 1

        if dict == {}:
            return 0

        return max(dict.values())

# Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
# Output: 16
    # def maxCandies(self,
    #                status: List[int],
    #                candies: List[int],
    #                keys: List[List[int]],
    #                containedBoxes: List[List[int]],
    #                initialBoxes: List[int]) -> int:

    #     def getCandies(self, i):
    #         if status[i] == 1 or i in self.hasKey:
    #             self.total += candies[i]

    #     self.total = 0
    #     self.hasKey = []
    #     for i in initialBoxes:
    #         self.hasKey.extend(keys[i])
    #         getCandies(self, i)

    #         for j in containedBoxes[i]:
    #             if keys[j]:
    #                 self.hasKey.extend(keys[j])

    #         for j in containedBoxes[i]:
    #             getCandies(self, j)

    #     return self.total
