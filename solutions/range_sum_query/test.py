import unittest
import range_sum_query.index as main


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [
            ([2, 7, 11, 15], 9),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                na = s.NumArray([-2, 0, 3, -5, 2, -1])
                self.assertEqual(na.sumRange(0, 2), 1)
                self.assertEqual(na.sumRange(2, 5), -1)
                self.assertEqual(na.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
