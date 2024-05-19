import unittest
import leftmost_column_with_at_least_a_one.index as main
from _class.binary_matrix import BinaryMatrix


class Test(unittest.TestCase):
    def test_leftMostColumnWithOne(self):
        test_patterns = [
            ([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]], 1),
            ([[0, 0], [0, 1]], 1),
            ([[0, 0], [1, 1]], 0),
            ([[0, 0], [0, 0]], -1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                bx: BinaryMatrix = BinaryMatrix(arg)
                self.assertEqual(s.leftMostColumnWithOne(bx), expected)


if __name__ == "__main__":
    unittest.main()
