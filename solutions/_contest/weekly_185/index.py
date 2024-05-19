from typing import List, Dict, Set, Tuple


class Solution:
    def reformat(self, s: str) -> str:
        import itertools

        string: str = ""
        i: str = ""
        for c in s:
            if str.isdigit(c):
                i += c
            else:
                string += c
        if len(i) > len(string):
            string, i = i, string
        if len(string) - len(i) > 1:
            return ""
        res: str = ""
        for f, s in itertools.zip_longest(string, i):
            res += f
            if s:
                res += s
        return res

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        orders.sort(key=lambda x: x[2])
        header: List[str] = []
        indexMap: Dict[int, List[int]] = {}
        for o in orders:
            if len(header) == 0 or header[-1] != o[2]:
                header.append(o[2])
                for k, v in indexMap.items():
                    indexMap[k] = v + [0]
            if int(o[1]) in indexMap:
                indexMap[int(o[1])][-1] += 1
            else:
                indexMap[int(o[1])] = [0] * len(header)
                indexMap[int(o[1])][-1] += 1
        sortedMap = sorted(indexMap.items())
        res: List[List[str]] = []
        res.append(["Table"] + header)
        for k, v in sortedMap:
            res.append([str(k)] + [str(x) for x in v])
        return res

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        char: Dict[str, int] = {"c": 0, "r": 0, "o": 0, "a": 0, "k": 0}
        prev: Dict[str, str] = {"r": "c", "o": "r", "a": "o", "k": "a"}
        res: int = 0
        for c in croakOfFrogs:
            char[c] += 1
            if c != "c" and char[c] > char[prev[c]]:
                return -1
            if c != "k":
                res = max(res, char[c] - char["k"])
        return res if char["c"] == char["k"] else -1

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7

        def dfs(i, j, k):
            if k < 0:
                return 0
            if i > n - 1:
                return k == 0
            cnt = 0
            for nj in range(1, j + 1):
                cnt = (cnt + dfs(i + 1, j, k)) % mod
            for nj in range(j + 1, m + 1):
                cnt = (cnt + dfs(i + 1, nj, k - 1)) % mod
            return cnt

        return dfs(0, 0, k)
