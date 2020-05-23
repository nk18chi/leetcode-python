import unittest
import solutions.interval_list_intersections.index as main


class Test(unittest.TestCase):
    def test_intervalIntersection(self):
        test_patterns = [
            ([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]], [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.intervalIntersection(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
