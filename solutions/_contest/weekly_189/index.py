from typing import List, Set, Tuple
import math


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res: int = 0
        for (s, e) in zip(startTime, endTime):
            if s <= queryTime <= e:
                res += 1
        return res

    def arrangeWords(self, text: str) -> str:
        arr: List[str] = text.split(" ")
        arr.sort(key=lambda x: len(x))
        return " ".join(arr).capitalize()

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        seen: List[Set[str]] = []
        res: List[int] = []
        addIndex: List[Tuple[int, List[str]]] = []
        for i, f in enumerate(favoriteCompanies):
            addIndex.append((i, f))
        addIndex.sort(key=lambda x: len(x[1]), reverse=True)
        for i, comp in addIndex:
            isMatch = False
            for s in seen:
                count: int = 0
                for c in comp:
                    if c in s:
                        count += 1
                    else:
                        break
                if count == len(comp):
                    isMatch = True
                if isMatch:
                    break
            if not isMatch:
                seen.append(set(comp))
                res.append(i)
        res.sort()
        return res

    def numPoints(self, points: List[List[int]], r: int) -> int:
        res: int = 1
        self.centers: List[List[float]] = []

        def setCenter(p1, p2):
            (x1, y1), (x2, y2) = p1, p2
            dx, dy = x2 - x1, y2 - y1
            q = math.sqrt(dx**2 + dy**2)
            if q > r * 2:
                return
            x3, y3 = (x1 + x2) / 2, (y1 + y2) / 2
            d = math.sqrt(r ** 2 - (q / 2) ** 2)
            self.centers.append([x3 - d * dy / q, y3 + d * dx / q])
            self.centers.append([x3 + d * dy / q, y3 - d * dx / q])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                setCenter(points[i], points[j])
        for c in self.centers:
            count: int = 0
            for p in points:
                count += 1 if (p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2 <= r ** 2 + 10 ** -6 else 0
            res = max(res, count)
        return res
