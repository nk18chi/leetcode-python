import unittest
import solutions.contiguous_array.index as main


class Test(unittest.TestCase):
    def test_findMaxLength(self):
        test_patterns = [
            ([0, 0, 1, 0, 0, 0, 1, 1], 6),
            ([0, 1, 0, 1], 4),
            ([0, 1], 2),
            ([0, 1, 0], 2)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findMaxLength(arg), expected)


if __name__ == '__main__':
    unittest.main()
