import unittest

import solutions.play_with_chips.index as main


class Test(unittest.TestCase):
    def test_minCostToMoveChips(self):
        test_patterns = [
            ([1, 2, 3], 1),
            ([2, 2, 2, 3, 3], 2)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minCostToMoveChips(arg), expected)


if __name__ == '__main__':
    unittest.main()
