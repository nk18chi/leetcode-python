from typing import List, Dict, Set, Tuple


class Solution:
    # # witout sorting
    # # Time complexity: O(n^2*S)
    # # Space complexity: O(n)
    # def stringMatching(self, words: List[str]) -> List[str]:
    #     res: List[str] = []
    #     for i in range(len(words)):
    #         for j in range(len(words)):
    #             if i != j and words[i] in words[j]:
    #                 res.append(words[i])
    #                 break
    #     return res

    # sorting
    # Time complexity: O(nlogn + n^2*S) -> O(n^2*S)
    # Space complexity: O(n)
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res: List[str] = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res: List[int] = []
        arr: List[int] = [i for i in range(1, m + 1)]
        for q in queries:
            index: int = arr.index(q)
            res.append(index)
            arr.insert(0, arr[index])
            del arr[index + 1]
        return res

    def entityParser(self, text: str) -> str:
        replaceMap: List[Tuple[str, str]] = [
            ("&quot;", "\""),
            ("&apos;", "'"),
            ("&gt;", ">"),
            ("&lt;", "<"),
            ("&frasl;", "/"),
            ("&amp;", "&"),
        ]
        for r in replaceMap:
            text = text.replace(r[0], r[1])
        return text
