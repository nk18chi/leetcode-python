# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/


def customSortString(S, T):

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
    print(customSortString("cba", "abcd"))
    print(customSortString("cba", "aafhouvavoabcac"))
