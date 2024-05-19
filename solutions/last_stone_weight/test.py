import unittest

import last_stone_weight.index as main


class Test(unittest.TestCase):
    def test_lastStoneWeight(self):
        test_patterns = [
            ([4, 4, 3, 3, 2, 2, 1, 1], 0),
            ([2, 7, 4, 1, 8, 1], 1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.lastStoneWeight(arg), expected)


if __name__ == "__main__":
    unittest.main()
