import unittest
import solutions._contest.weekly_166.index as main


class Test(unittest.TestCase):

    def test_subtractProductAndSum(self):
        test_patterns = [
            (234, 15),
            (4421, 21),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.subtractProductAndSum(arg), expected)

    def test_groupThePeople(self):
        test_patterns = [
            ([2, 1, 3, 3, 3, 2], [[0, 5], [1], [2, 3, 4]]),
            ([3, 3, 3, 3, 3, 1, 3], [[0, 1, 2], [3, 4, 6], [5]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.groupThePeople(arg), expected)


if __name__ == '__main__':
    unittest.main()
