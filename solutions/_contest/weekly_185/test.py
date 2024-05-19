import unittest
import _contest.weekly_185.index as main


class Test(unittest.TestCase):
    def test_reformat(self):
        test_patterns = [
            ("covid2019", "c2o0v1i9d"),
            ("a0b1c2", "a0b1c2"),
            ("leetcode", ""),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.reformat(arg), expected)

    def test_displayTable(self):
        test_patterns = [
            (
                [
                    ["David", "3", "Ceviche"],
                    ["Corina", "10", "Beef Burrito"],
                    ["David", "3", "Fried Chicken"],
                    ["Carla", "5", "Water"],
                    ["Carla", "5", "Ceviche"],
                    ["Rous", "3", "Ceviche"],
                ],
                [
                    ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"],
                    ["3", "0", "2", "1", "0"],
                    ["5", "0", "1", "0", "1"],
                    ["10", "1", "0", "0", "0"],
                ],
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.displayTable(arg), expected)

    def test_minNumberOfFrogs(self):
        test_patterns = [
            ("croakcroa", -1),
            ("crcoakroak", 2),
            ("croakcroak", 1),
            ("croakcrook", -1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minNumberOfFrogs(arg), expected)

    def test_numOfArrays(self):
        test_patterns = [
            (2, 3, 1, 6),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numOfArrays(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
