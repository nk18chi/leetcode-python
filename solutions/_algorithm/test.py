import unittest
import solutions._algorithm.search as search
import solutions._algorithm.sort as sort


class Test(unittest.TestCase):
    def test_linearSearch(self):
        test_patterns = [
            ([1, 2, 3, 4, 5], 9, -1),
            ([1, 2, 3, 4, 5], 4, 3)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = search.Search()
                self.assertEqual(s.linearSearch(arg1, arg2), expected)

    def test_binarySearch(self):
        test_patterns = [
            ([1, 2, 3, 4, 5], 0, 4, 9, -1),
            ([1, 2, 3, 4, 5], 0, 4, 4, 3)
        ]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = search.Search()
                self.assertEqual(s.binarySearch(arg1, arg2, arg3, arg4), expected)

    def test_bubbleSort(self):
        test_patterns = [
            ([4, 3, 2, 5, 1], [1, 2, 3, 4, 5]),
            ([2, 3, 4, 5, 1], [1, 2, 3, 4, 5])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = sort.Sort()
                self.assertEqual(s.bubbleSort(arg), expected)

    def test_selectionSort(self):
        test_patterns = [
            ([4, 3, 2, 5, 1], [1, 2, 3, 4, 5]),
            ([2, 3, 4, 5, 1], [1, 2, 3, 4, 5])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = sort.Sort()
                self.assertEqual(s.selectionSort(arg), expected)

    def test_insertionSort(self):
        test_patterns = [
            ([4, 3, 2, 5, 1], [1, 2, 3, 4, 5]),
            ([2, 3, 4, 5, 1], [1, 2, 3, 4, 5])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = sort.Sort()
                self.assertEqual(s.insertionSort(arg), expected)

    def test_mergeSort(self):
        test_patterns = [
            ([4, 3, 2, 5, 1], [1, 2, 3, 4, 5]),
            ([2, 3, 4, 5, 1], [1, 2, 3, 4, 5])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = sort.Sort()
                self.assertEqual(s.mergeSort(arg), expected)

    def test_quickSort(self):
        test_patterns = [
            ([4, 3, 2, 5, 1], [1, 2, 3, 4, 5]),
            ([2, 3, 4, 5, 1], [1, 2, 3, 4, 5])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = sort.Sort()
                self.assertEqual(s.quickSort(arg), expected)


if __name__ == '__main__':
    unittest.main()
