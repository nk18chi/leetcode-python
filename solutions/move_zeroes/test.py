import unittest
import solutions.move_zeroes.index as main


class Test(unittest.TestCase):
    def test_moveZeroes(self):
        test_patterns = [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                s.moveZeroes(arg)
                self.assertEqual(arg, expected)


if __name__ == '__main__':
    unittest.main()
