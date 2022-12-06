# 38. Count and Say
# https://leetcode.com/problems/count-and-say/


class Solution:
    # Time complexity: O(N^2)
    # Space complexity: O(1)
    def countAndSay(self, n: int) -> str:
        res: str = "1"
        for _ in range(2, n + 1):
            newRes: str = ""
            count: int = 1
            for j in range(len(res)):
                if j + 1 < len(res) and res[j] == res[j + 1]:
                    count += 1
                else:
                    newRes += str(count) + str(res[j])
                    count = 1
            res = newRes
        return res
