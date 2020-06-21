import unittest
import solutions._contest.weekly_194.index as main


class Test(unittest.TestCase):
    def test_xorOperation(self):
        test_patterns = [
            (5, 0, 8),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.xorOperation(arg1, arg2), expected)

    def test_getFolderNames(self):
        test_patterns = [
            (["kaido", "kaido(1)", "kaido", "kaido(1)", "kaido(2)"], ["kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)", "kaido(2)(1)"]),
            (["gta", "gta(1)", "gta", "avalon"], ["gta", "gta(1)", "gta(2)", "avalon"]),
            (["pes", "fifa", "gta", "pes(2019)"], ["pes", "fifa", "gta", "pes(2019)"]),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.getFolderNames(arg1), expected)

    def test_avoidFlood(self):
        test_patterns = [
            ([2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2], []),
            ([1, 0, 2, 0], [-1, 1, -1, 1]),
            ([69, 0, 0, 0, 69], [-1, 69, 1, 1, -1]),
            ([1, 2, 0, 0, 2, 1], [-1, -1, 2, 1, -1, -1]),
            ([1, 2, 3, 4], [-1, -1, -1, -1]),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.avoidFlood(arg1), expected)


if __name__ == '__main__':
    unittest.main()
