import unittest
import uncrossed_lines.index as main


class Test(unittest.TestCase):
    def test_maxUncrossedLines(self):
        test_patterns = [
            ([1, 4, 2], [1, 2, 4], 2),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxUncrossedLines(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
