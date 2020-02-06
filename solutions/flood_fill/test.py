import unittest

import solutions.flood_fill.index as main


class Test(unittest.TestCase):

    def test_floodFill(self):
        test_patterns = [([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2,
                          [[2, 2, 2], [2, 2, 0], [2, 0, 1]])]

        for i, (arg1, arg2, arg3, arg4, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.floodFill(arg1, arg2, arg3, arg4), expected)


if __name__ == '__main__':
    unittest.main()
