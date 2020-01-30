import unittest
import importlib
f = importlib.import_module('solutions.1046_last_stone_weight.index')


class Test(unittest.TestCase):
    def test_lastStoneWeight(self):
        test_patterns = [
            ([4, 4, 3, 3, 2, 2, 1, 1], 0),
            ([2, 7, 4, 1, 8, 1], 1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.lastStoneWeight(arg), expected)


if __name__ == '__main__':
    unittest.main()
