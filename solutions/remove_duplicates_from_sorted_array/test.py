import unittest
import solutions.remove_duplicates_from_sorted_array.index as main


class Test(unittest.TestCase):
    def test_removeDuplicates(self):
        test_patterns = [
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
            ([1, 1, 2], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.removeDuplicates(arg), expected)


if __name__ == '__main__':
    unittest.main()
