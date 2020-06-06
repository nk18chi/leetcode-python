# 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/

from typing import List


class Solution:
    # Time complexity: O(n^2)
    # Time complexity: O(1)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res: List[List[int]] = []
        for p in people:
            res.insert(p[1], p)
        return res
