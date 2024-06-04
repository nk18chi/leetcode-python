from typing import List


class Solution:
    def minimumChairs(self, s: str) -> int:
        result: int = 0
        count: int = 0
        for c in s:
            if c == "E":
                count += 1
                result = max(result, count)
            else:
                count -= 1
        return result

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        availability: int = meetings[0][0] - 1
        for i in range(1, len(meetings)):
            if meetings[i - 1][1] < meetings[i][0]:
                availability += meetings[i][0] - meetings[i - 1][1] - 1
            elif meetings[i - 1][1] > meetings[i][1]:
                meetings[i][1] = meetings[i - 1][1]
        availability += days - meetings[-1][1]
        return availability

    def clearStars(self, s: str) -> str:
        result: List[str] = list(s)
        alphabet: List[List[int]] = [[]]
        for i in range(26):
            alphabet.append([])
        for i in range(len(s)):
            if s[i] == "*":
                for i in range(len(alphabet)):
                    if len(alphabet[i]) == 0:
                        continue
                    n: int = alphabet[i].pop()
                    result[n] = "*"
                    break
            else:
                index: int = ord(s[i]) - ord("a")
                alphabet[index].append(i)

        return "".join(result).replace("*", "")
