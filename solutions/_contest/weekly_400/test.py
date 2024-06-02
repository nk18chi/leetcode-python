import unittest
import _contest.weekly_400.index as main


class Test(unittest.TestCase):
    def test_numberOfPairs(self):
        test_patterns = [
            ([1, 2, 4, 12], [2, 4], 3, 2),
        ]
        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numberOfPairs(arg1, arg2, arg3), expected)

    def test_compressedString(self):
        test_patterns = [
            ("aaaaaaaaaaaaaabb", "9a5a2b"),
        ]
        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.compressedString(arg1), expected)

    def test_numberOfPairs2(self):
        test_patterns = [([4, 8, 4, 8], [1, 2, 1, 2], 2, 16)]
        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numberOfPairs2(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
