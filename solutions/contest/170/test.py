import unittest
import importlib
f = importlib.import_module('solutions.contest.170.index')


class Test(unittest.TestCase):
    def test_xorQueries(self):
        test_patterns = [
            ([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [3, 3]], [2, 7, 12, 8]),
            ([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]], [8, 0, 4, 4])
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.xorQueries(arg1, arg2), expected)

    def test_freqAlphabets(self):
        test_patterns = [
            ("10#11#12",
             "jkab"),
            ("1326#",
             "acz"),
            ("25#",
             "y"),
            ("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#",
             "abcdefghijklmnopqrstuvwxyz")]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.freqAlphabets(arg1), expected)


if __name__ == '__main__':
    unittest.main()
