# the question from Derrick, who is my teacher

from typing import List

# 51
# 17
# 16
# 15, 8
# 5, 4
# 4, 2
# 2, 1


class Solution:
    def make_one(self, n: int) -> int:
        list: List[int] = [n]
        count: int = 0
        while min(list) > 1:
            for i in range(len(list)):
                if list[i] % 3 == 0:
                    list[i] = list[i] // 3
                else:
                    if list[i] % 2 == 0:
                        list.append(list[i] // 2)
                    list[i] -= 1
            count += 1
        return count
