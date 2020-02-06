# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/


def main():
    solution = Solution()
    print(solution.customSortString("cba", "abcd"))
    print(solution.customSortString("cba", "aafhouvavoabcac"))


class Solution:
    def customSortString(self, S: str, T: str) -> str:

        dict = {}
        for s in S:
            dict[s] = 0

        not_match = ""
        for t in T:
            match = False
            for s in S:
                if t == s:
                    dict[t] += 1
                    match = True
                    break

            if not match:
                not_match += t

        str = ""
        for k, v in dict.items():
            str += k * v
        str += not_match

        return str


if __name__ == '__main__':
    main()
