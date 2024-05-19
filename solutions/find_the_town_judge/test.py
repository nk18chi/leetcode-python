import unittest
import find_the_town_judge.index as main


class Test(unittest.TestCase):
    def test_findJudge(self):
        test_patterns = [
            (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
            (3, [[1, 2], [2, 3]], -1),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findJudge(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
