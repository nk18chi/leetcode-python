import unittest
import possible_bipartition.index as main


class Test(unittest.TestCase):
    def test_possibleBipartition(self):
        test_patterns = [
            (5, [[1, 2], [3, 4], [4, 5], [3, 5]], False),
            (4, [[1, 2], [1, 3], [2, 4]], True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.possibleBipartition(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
