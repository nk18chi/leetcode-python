import unittest
import solutions.search_insert_position.index as main


class Test(unittest.TestCase):
    def test_searchInsert(self):
        test_patterns = [
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
            ([1, 3, 5, 6], 0, 0)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.searchInsert(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
