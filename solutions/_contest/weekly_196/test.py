import unittest
import solutions._contest.weekly_196.index as main


class Test(unittest.TestCase):
    def test_numSubmat(self):
        test_patterns = [
            ([[0, 1, 1, 0],
              [0, 1, 1, 1],
              [1, 1, 1, 0]], 24),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numSubmat(arg), expected)


if __name__ == '__main__':
    unittest.main()
