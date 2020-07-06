import unittest
import solutions.plus_one.index as main


class Test(unittest.TestCase):
    def test_plusOne(self):
        test_patterns = [
            ([1, 2, 3], [1, 2, 4]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.plusOne(arg), expected)


if __name__ == '__main__':
    unittest.main()
