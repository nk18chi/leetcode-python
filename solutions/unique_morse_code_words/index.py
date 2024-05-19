# 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/

from typing import List, Set


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code: List[str] = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        transformations: Set[str] = set()
        for word in words:
            string: str = ""
            for c in word:
                string += morse_code[ord(c) - 97]
            transformations.add(string)
        return len(transformations)
