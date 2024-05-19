import unittest
import word_ladder.index as main


class Test(unittest.TestCase):
    def test_ladderLength(self):
        test_patterns = [
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
        ]

        for i, (arg1, arg2, arg3, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.ladderLength(arg1, arg2, arg3), expected)


if __name__ == "__main__":
    unittest.main()
