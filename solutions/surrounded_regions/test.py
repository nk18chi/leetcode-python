import unittest
import surrounded_regions.index as main


class Test(unittest.TestCase):
    def test_solve(self):
        test_patterns = [
            (
                [
                    ["X", "X", "X", "X"],
                    ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"],
                    ["X", "O", "X", "X"],
                ],
                [
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "O", "X", "X"],
                ],
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                s.solve(arg)
                self.assertEqual(arg, expected)


if __name__ == "__main__":
    unittest.main()
