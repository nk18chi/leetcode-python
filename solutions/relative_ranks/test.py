import unittest
import solutions.relative_ranks.index as main


class Test(unittest.TestCase):
    def test_findRelativeRanks(self):
        test_patterns = [
            ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findRelativeRanks(arg), expected)


if __name__ == '__main__':
    unittest.main()
