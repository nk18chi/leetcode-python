import unittest
import escape_the_ghosts.index as main


class Test(unittest.TestCase):
    def test_escapeGhosts(self):
        test_patterns = [
            ([[1, 0], [0, 3]], [0, 1], True),
            ([[1, 0]], [2, 0], False),
            ([[2, 0]], [1, 0], False),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.escapeGhosts(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
