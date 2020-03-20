import unittest
import solutions.distance_between_bus_stops.index as main


class Test(unittest.TestCase):
    def test_distanceBetweenBusStops(self):
        test_patterns = [
            ([1, 2, 3, 4], 0, 3, 4),
            ([1, 2, 3, 4], 0, 1, 1),
            ([6, 47, 48, 31, 10, 27, 46, 33, 52, 33, 38, 25, 32, 45, 36, 3, 0, 33, 22, 53, 8, 13, 18, 1, 44, 41, 14, 5, 38, 25, 48], 22, 0, 234),
            ([7, 10, 1, 12, 11, 14, 5, 0], 7, 2, 17),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.distanceBetweenBusStops(arg1, arg2, arg3), expected)


if __name__ == '__main__':
    unittest.main()
