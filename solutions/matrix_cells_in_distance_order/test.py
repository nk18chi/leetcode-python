import unittest

import matrix_cells_in_distance_order.index as main


class Test(unittest.TestCase):
    def test_allCellsDistOrder(self):
        test_patterns = [
            (2, 3, 1, 2, [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]),
            # (2, 3, 1, 2, [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]),
            # (2, 2, 0, 1, [[0, 1], [0, 0], [1, 1], [1, 0]]),
            # (1, 2, 0, 0, [[0, 0], [0, 1]]),
        ]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.allCellsDistOrder(arg1, arg2, arg3, arg4), expected)


if __name__ == "__main__":
    unittest.main()
