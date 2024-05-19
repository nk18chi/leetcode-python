import unittest
import cells_with_odd_values_in_a_matrix.index as main


class Test(unittest.TestCase):
    def test_oddCells(self):
        test_patterns = [
            (2, 3, [[0, 1], [1, 1]], 6),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.oddCells(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
