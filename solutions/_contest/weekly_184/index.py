from typing import List, Dict, Set, Tuple


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res: List[str] = []
        for _ in range(len(words)):
            target = words[0]
            del words[0]
            for word in words:
                if target in word:
                    res.append(target)
                    break
            words.append(target)
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
