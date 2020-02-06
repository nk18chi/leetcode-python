# 520. Detect Capital
# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True

        if word[0].isupper() and word[1:].islower():
            return True

        return False

        # second solution
        # return word.isupper() or word.islower() or word.istitle()
