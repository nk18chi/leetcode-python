import unittest
import insert_interval.index as main


class Test(unittest.TestCase):
    def test_insert(self):
        test_patterns = [
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            (
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                [4, 8],
                [[1, 2], [3, 10], [12, 16]],
            ),
            ([[2, 3], [6, 9]], [0, 1], [[0, 1], [2, 3], [6, 9]]),
            ([], [2, 5], [[2, 5]]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.insert(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
