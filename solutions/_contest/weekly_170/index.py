from typing import List

# Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# Output: [2,7,14,8]
# Explanation:
# The binary representation of the elements in the array are:
# 1 = 0001
# 3 = 0011
# 4 = 0100
# 8 = 1000
# The XOR values for queries are:
# [0,1] = 1 xor 3 = 2
# [1,2] = 3 xor 4 = 7
# [0,3] = 1 xor 3 xor 4 xor 8 = 14
# [3,3] = 8


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(arr) - 1):
            arr[i + 1] ^= arr[i]
        list = []
        for q in queries:
            if q[0] == 0:
                list.append(arr[q[1]])
            else:
                list.append(arr[q[1]] ^ arr[q[0] - 1])
        return list

        # list = []
        # for query in queries:
        #     res = arr[query[0]]
        #     for i in range(query[0] + 1, query[1] + 1):
        #         res = res ^ arr[i]
        #     list.append(res)
        # return list

        # list = []
        # for query in queries:
        #     if query[0] == query[1]:
        #         list.append(arr[query[0]])
        #     else:
        #         list.append(dict[str(query[0]) + ',' + str(query[1])])
        # return list

    def freqAlphabets(self, s: str) -> str:
        dict = {
            "1": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "10#": "j",
            "11#": "k",
            "12#": "l",
            "13#": "m",
            "14#": "n",
            "15#": "o",
            "16#": "p",
            "17#": "q",
            "18#": "r",
            "19#": "s",
            "20#": "t",
            "21#": "u",
            "22#": "v",
            "23#": "w",
            "24#": "x",
            "25#": "y",
            "26#": "z",
        }

        res = text = ""
        for c in s[::-1]:
            text = c + text
            if text in dict:
                res = dict[text] + res
                text = ""

        return res
