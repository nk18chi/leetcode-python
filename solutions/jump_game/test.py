import unittest
import jump_game.index as main


class Test(unittest.TestCase):
    def test_canJump(self):
        test_patterns = [
            ([2, 3, 1, 1, 4], True),
            ([4, 3, 2, 1, 0, 0], False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.canJump(arg), expected)


if __name__ == "__main__":
    unittest.main()
