# 443. String Compression - Easy
# https://leetcode.com/problems/string-compression/

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars) <= 1:
            return len(chars)

        target = chars[0]
        count = 1
        index = 1
        num = 1
        for c in chars[1:]:
            chars[num] = None
            if target == c:
                count = count + 1
            else:
                if count != 1:
                    for s in str(count):
                        chars[index] = s
                        index = index + 1
                chars[index] = c
                index = index + 1
                count = 1
            target = c
            num = num + 1

        if 1 < count:
            for s in str(count):
                chars[index] = s
                index = index + 1

        chars = [x for x in chars if x is not None]

        return len(chars)
