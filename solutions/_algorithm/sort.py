from typing import List


class Sort:
    def bubbleSort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            for j in range(1, len(arr) - i):
                if arr[j - 1] > arr[j]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return arr

    def selectionSort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            min_index: int = i
            for j in range(i + 1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    def insertionSort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
        return arr

    def mergeSort(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr
        mid: int = len(arr) // 2
        L: List[int] = self.mergeSort(arr[:mid])
        R: List[int] = self.mergeSort(arr[mid:])

        i: int = 0
        j: int = 0
        res: List[int] = []
        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            else:
                res.append(R[j])
                j += 1
        if i < j:
            res.extend(L[i:])
        else:
            res.extend(R[j:])

        return res

    def quickSort(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr

        target: int = arr[0]
        L: List[int] = []
        R: List[int] = []
        for n in arr[1:]:
            if n < target:
                L.append(n)
            else:
                R.append(n)

        res: List[int] = []
        res.extend(self.quickSort(L))
        res.append(target)
        res.extend(self.quickSort(R))

        return res
