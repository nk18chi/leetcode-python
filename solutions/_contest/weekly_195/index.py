from typing import List, Set, Dict, Tuple


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen: Set[Tuple[int, int]] = set()
        seen.add((0, 0))
        row: int = 0
        col: int = 0
        for p in path:
            if p == "N":
                row += 1
            elif p == "S":
                row -= 1
            elif p == "E":
                col += 1
            else:
                col -= 1
            if (row, col) in seen:
                return True
            seen.add((row, col))
        return False

    def canArrange(self, arr: List[int], k: int) -> bool:
        seen: Dict[int, int] = {}
        for a in arr:
            modulo: int = abs(a) % k
            if a < 0:
                modulo *= -1
            minus: int = a % k * -1
            plus: int = k + minus
            if modulo in seen and seen[modulo] > 0:
                seen[modulo] -= 1
                seen[modulo + k if modulo <= 0 else modulo - k] -= 1
                continue
            seen[minus] = seen.get(minus, 0) + 1
            seen[plus] = seen.get(plus, 0) + 1
        for s in seen.values():
            if s != 0:
                return False
        return True
