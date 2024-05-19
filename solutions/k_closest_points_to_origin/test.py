import unittest
import k_closest_points_to_origin.index as main


class Test(unittest.TestCase):
    def test_kClosest(self):
        test_patterns = [
            ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
            ([[3, 3], [5, -1], [-2, 4]], 2, [[-2, 4], [3, 3]]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.kClosest(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
