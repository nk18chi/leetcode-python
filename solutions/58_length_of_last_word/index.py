# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

# from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # # third solution
        # list = s.strip().split(" ")
        # if len(list) == 0:
        #     return 0
        # return len(list[-1])

        # second solution
        countOfLastWord = 0
        for c in s[::-1]:
            if c == " ":
                if countOfLastWord > 0:
                    return countOfLastWord
                continue
            else:
                countOfLastWord += 1
        return countOfLastWord

        # # first solution
        # countOfLastWord = 0
        # resetFlag = False
        # for c in s:
        #     if c == " ":
        #         resetFlag = True
        #     else:
        #         if resetFlag:
        #             countOfLastWord = 0
        #             resetFlag = False
        #         countOfLastWord += 1

        # return countOfLastWord
