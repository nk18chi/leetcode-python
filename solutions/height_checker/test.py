import unittest
import solutions.height_checker.index as main


class Test(unittest.TestCase):
    def test_heightChecker(self):
        test_patterns = [
            ([1, 1, 4, 2, 1, 3], 3)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.heightChecker(arg), expected)


if __name__ == '__main__':
    unittest.main()
