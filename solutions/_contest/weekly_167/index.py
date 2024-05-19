from typing import List

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

# Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# Output: 3
#
# 1111
# 1000
# 1000
# 1000


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        len_height = len(mat)
        len_width = len(mat[0])
        max_length = min(len_height, len_width)

        while max_length > 0:
            for i in range(0, len_height):
                sum_list: List[int] = []
                row_count = 1
                for m in mat[i:]:
                    list = []
                    for j in range(0, len_width):
                        list.append(sum(m[j : j + max_length]))
                    if row_count <= max_length:
                        if not sum_list:
                            sum_list = list[::]
                        else:
                            for index, l in enumerate(list):
                                sum_list[index] += l
                    if row_count == max_length:
                        for s in sum_list:
                            if s <= threshold:
                                return max_length
                        row_count = 0
                        sum_list = []
                    row_count += 1
                max_length -= 1

        return 0

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_digits = len(str(low)) - 1
        target = low
        list = []
        while target <= high:
            i = target // (10**low_digits)
            if i > 9 - low_digits:
                low_digits += 1
                target = 10**low_digits
                continue
            else:
                sum = 0
                count = 0
                j = i
                for _ in range(low_digits, -1, -1):
                    sum += i * (10 ** (low_digits - count))
                    i += 1
                    count += 1
                if sum < low:
                    target = (j + 1) * (10**low_digits)
                elif sum > high:
                    break
                else:
                    list.append(sum)
                    target = (j + 1) * (10**low_digits)

        return list
