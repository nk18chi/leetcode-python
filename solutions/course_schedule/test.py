import unittest
import course_schedule.index as main


class Test(unittest.TestCase):
    def test_canFinish(self):
        test_patterns = [
            (8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]], True),
            (2, [[0, 1]], True),
            (6, [[1, 0], [2, 0], [2, 5], [3, 2], [5, 1], [4, 2]], True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.canFinish(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
