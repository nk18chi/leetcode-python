import unittest
import solutions.coin_change_2.index as main


class Test(unittest.TestCase):
    def test_change(self):
        test_patterns = [
            (7, [2, 5, 7], 2),
            (5, [1, 2, 5], 4),
            (500, [1, 2, 5], 12701),
            (0, [], 1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.change(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
