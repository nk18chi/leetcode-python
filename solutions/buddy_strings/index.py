# 859. Buddy Strings - Easy
# https://leetcode.com/problems/buddy-strings/


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) < 2 or len(B) < 2 or len(A) != len(B):
            return False

        if A == B and len(set(A)) != len(A):
            return True

        aList = []
        bList = []
        for a, b in zip(A, B):
            if a != b:
                aList.append(a)
                bList.append(b)

        if len(aList) != 2:
            return False
        return aList[0] == bList[1] and aList[1] == bList[0]
