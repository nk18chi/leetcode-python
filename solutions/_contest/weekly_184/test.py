import unittest
import solutions._contest.weekly_184.index as main


class Test(unittest.TestCase):
    def test_stringMatching(self):
        test_patterns = [
            (["mass", "as", "hero", "superhero"], ["as", "hero"]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.stringMatching(arg), expected)

    def test_processQueries(self):
        test_patterns = [
            ([8, 7, 4, 2, 8, 1, 7, 7], 8, [7, 7, 5, 4, 3, 4, 4, 0]),
            ([7, 5, 5, 8, 3], 8, [6, 5, 0, 7, 5]),
            ([4, 1, 2, 2], 4, [3, 1, 2, 0]),
            ([3, 1, 2, 1], 5, [2, 1, 2, 1]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.processQueries(arg1, arg2), expected)

    def test_entityParser(self):
        test_patterns = [
            ("&amp;gt;", "&gt;"),
            ("&amp; is an HTML entity but &ambassador; is not.", "& is an HTML entity but &ambassador; is not."),
            ("and I quote: &quot;...&quot;", "and I quote: \"...\""),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.entityParser(arg), expected)


if __name__ == '__main__':
    unittest.main()
