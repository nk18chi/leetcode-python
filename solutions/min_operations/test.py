import unittest
import min_operations.index as main


class Test(unittest.TestCase):
    def test_minOperations(self):
        test_patterns = [
            ([2, 3, 3, 2, 2, 4, 2, 3, 4], 4),
            ([2, 1, 2, 2, 3, 3], -1),
            (
                [
                    14,
                    12,
                    14,
                    14,
                    12,
                    14,
                    14,
                    12,
                    12,
                    12,
                    12,
                    14,
                    14,
                    12,
                    14,
                    14,
                    14,
                    12,
                    12,
                ],
                7,
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minOperations(arg), expected)


if __name__ == "__main__":
    unittest.main()
