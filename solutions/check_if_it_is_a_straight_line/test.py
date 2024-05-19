import unittest
import check_if_it_is_a_straight_line.index as main


class Test(unittest.TestCase):
    def test_checkStraightLine(self):
        test_patterns = [
            ([[0, 1], [1, 3], [-4, -7], [5, 11]], True),
            ([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]], True),
            ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
            ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
            (
                [
                    [-7, -3],
                    [-7, -1],
                    [-2, -2],
                    [0, -8],
                    [2, -2],
                    [5, -6],
                    [5, -5],
                    [1, 7],
                ],
                False,
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.checkStraightLine(arg), expected)


if __name__ == "__main__":
    unittest.main()
