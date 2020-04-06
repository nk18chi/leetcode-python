# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List, Dict

class Solution:
    # O(n * mLogm) in time, O(n * m) in space.
    # n is the number of strings in a given arr(strs).
    # m is the length of each string.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[str, List[str]] = {}
        for s in strs:
            key: str = "".join(sorted(s))
            groups[key] = groups.get(key, []) + [s]
        return list(groups.values())
