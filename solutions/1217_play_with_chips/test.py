import unittest
import importlib
f = importlib.import_module('solutions.1217_play_with_chips.index')


class Test(unittest.TestCase):
    def test_minCostToMoveChips(self):
        test_patterns = [
            ([1, 2, 3], 1),
            ([2, 2, 2, 3, 3], 2)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.minCostToMoveChips(arg), expected)


if __name__ == '__main__':
    unittest.main()
