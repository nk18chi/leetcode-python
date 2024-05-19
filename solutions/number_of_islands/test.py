import unittest
import number_of_islands.index as main


class Test(unittest.TestCase):
    def test_numIslands(self):
        test_patterns = [
            (
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ],
                1,
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numIslands(arg), expected)


if __name__ == "__main__":
    unittest.main()
