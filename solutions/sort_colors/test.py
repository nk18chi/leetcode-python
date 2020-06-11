import unittest
import solutions.sort_colors.index as main


class Test(unittest.TestCase):
    def test_sortColors(self):
        test_patterns = [
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                s.sortColors(arg)
                self.assertEqual(arg, expected)


if __name__ == '__main__':
    unittest.main()
