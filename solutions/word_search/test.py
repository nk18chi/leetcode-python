import unittest
import word_search.index as main


class Test(unittest.TestCase):
    def test_exist(self):
        test_patterns = [
            (
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED",
                True,
            ),
            (
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "SEE",
                True,
            ),
            (
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB",
                False,
            ),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.exist(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
