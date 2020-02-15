# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

from typing import List, Dict

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


class Solution:
    # # first solution
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res: List[List[str]] = []
    #     alphabetList: List[List[int]] = []
    #     for s in strs:
    #         alphabet: List[int] = [0] * 27
    #         for c in s:
    #             index: int = ord(c) - 97
    #             alphabet[index] += 1
    #         isMatch = False
    #         if len(alphabetList) > 0:
    #             for i in range(len(alphabetList)):
    #                 if alphabetList[i] == alphabet:
    #                     res[i].append(s)
    #                     isMatch = True
    #         if not isMatch:
    #             res.append([s])
    #             alphabetList.append(alphabet)

    #     return res

    # second solution
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict: Dict[str, List[str]] = {}
        for s in strs:
            key: str = "".join(sorted(s))
            dict[key] = dict.get(key, []) + [s]
        return list(dict.values())
