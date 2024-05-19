import unittest
import available_captures_for_rook.index as main


class Test(unittest.TestCase):
    def test_numRookCaptures(self):
        test_patterns = [
            (
                [
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", "p", "p", "p", "p", "p", ".", "."],
                    [".", "p", "p", "B", "p", "p", ".", "."],
                    [".", "p", "B", "R", "B", "p", ".", "."],
                    [".", "p", "p", "B", "p", "p", ".", "."],
                    [".", "p", "p", "p", "p", "p", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                ],
                0,
            ),
            (
                [
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", "p", ".", ".", ".", "."],
                    [".", ".", ".", "R", ".", ".", ".", "p"],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", "p", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."],
                ],
                3,
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numRookCaptures(arg), expected)


if __name__ == "__main__":
    unittest.main()
