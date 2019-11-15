# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/


def generate(numRows):
    initial = 1
    list = []

    if 0 == numRows:
        return list

    list.append([initial])

    for i in range(initial, numRows):
        list.append([0] * (i + 1))

        j = 0
        for li in list[i - 1]:
            list[i][j] += li
            list[i][j + 1] += li
            j += 1

    return list


if __name__ == '__main__':
    print(generate(0))
    print(generate(1))
    print(generate(5))
    print(generate(10))
