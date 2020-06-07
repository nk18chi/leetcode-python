import unittest
import solutions._contest.weekly_192.index as main


class Test(unittest.TestCase):
    def test_shuffle(self):
        test_patterns = [
            ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.shuffle(arg1, arg2), expected)

    def test_getStrongest(self):
        test_patterns = [
            ([-7, 22, 17, 3], 2, [22, 17]),
            ([1, 2, 3, 4, 5], 2, [5, 1]),
            ([1, 1, 3, 5, 5], 2, [5, 5]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getStrongest(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
