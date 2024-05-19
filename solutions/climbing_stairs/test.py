import unittest
import climbing_stairs.index as main


class Test(unittest.TestCase):
    def test_climbStairs(self):
        test_patterns = [(2, 2), (3, 3)]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.climbStairs(arg), expected)


if __name__ == "__main__":
    unittest.main()
