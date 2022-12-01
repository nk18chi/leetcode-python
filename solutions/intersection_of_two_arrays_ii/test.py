import unittest
import solutions.intersection_of_two_arrays_ii.index as main


class Test(unittest.TestCase):
    def test_intersect(self):
        test_patterns = [
            ([1, 2, 2, 1], [2, 2], [2, 2]),
            ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4])
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.intersect(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
