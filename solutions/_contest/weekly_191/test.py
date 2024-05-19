import unittest
import _contest.weekly_191.index as main


class Test(unittest.TestCase):
    def test_minReorder(self):
        test_patterns = [
            (5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minReorder(arg1, arg2), expected)

    # def test_getProbability(self):
    #     test_patterns = [
    #         ([6, 6, 6, 6, 6, 6], 0.90327),
    #     ]

    #     for i, (arg, expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = main.Solution()
    #             self.assertEqual(s.getProbability(arg), expected)


if __name__ == "__main__":
    unittest.main()
