from typing import List, Set, Dict


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        fir: int = 0
        sec: int = len(nums) // 2
        res: List[int] = []
        while sec < len(nums):
            res.append(nums[fir])
            res.append(nums[sec])
            fir += 1
            sec += 1
        return res

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        indexArr: List[List[int]] = [[i, n] for i, n in enumerate(arr)]
        indexArr.sort(key=lambda x: x[1])
        midian: int = indexArr[(len(arr) - 1) // 2][1]
        for n in indexArr:
            n.append(abs(midian - n[1]))
        indexArr.sort(key=lambda x: (-x[2], -x[1]))
        return [indexArr[i][1] for i in range(k)]

    class BrowserHistory:
        def __init__(self, homepage: str):
            self.q: List[str] = [homepage]
            self.cur: int = 0

        def visit(self, url: str) -> None:
            self.q = self.q[:self.cur + 1]
            self.q.append(url)
            self.cur += 1

        def back(self, steps: int) -> str:
            self.cur -= steps
            if self.cur < 0:
                self.cur = 0
            return self.q[self.cur]

        def forward(self, steps: int) -> str:
            self.cur += steps
            if self.cur >= len(self.q):
                self.cur = len(self.q) - 1
            return self.q[self.cur]
