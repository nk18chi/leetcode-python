# 299. Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/

# from typing import List


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        s_wrong, g_wrong = [], []
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                s_wrong += s
                g_wrong += g

        for g in g_wrong:
            if g in s_wrong:
                cow += 1
                s_wrong.remove(g)

        return "{}A{}B".format(bull, cow)
