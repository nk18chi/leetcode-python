from typing import List, Dict


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            left: int = nums[i - 1] % 2
            right: int = nums[i] % 2
            if left == right:
                return False
        return True

    def isArraySpecial2(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        sum: List[int] = [0] * len(nums)
        for i in range(1, len(nums)):
            sum[i] = sum[i - 1]
            if nums[i - 1] % 2 != nums[i] % 2:
                sum[i] += 1
        result: List[bool] = []
        for query in queries:
            expect: int = query[1] - query[0]
            actual: int = sum[query[1]] - sum[query[0]]
            if expect == actual:
                result.append(True)
            else:
                result.append(False)
        return result

    def sumDigitDifferences(self, nums: List[int]) -> int:
        length: int = len(nums)
        result: int = length * (length - 1) // 2 * len(str(nums[0]))
        for digit in range(len(str(nums[0]))):
            counter: Dict[str, int] = {}
            for num in nums:
                n: int = str(num)[digit]
                if n not in counter:
                    counter[n] = 0
                result -= counter[n]
                counter[n] += 1
        return result
