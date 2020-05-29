import unittest
import solutions.counting_bits.index as main


class Test(unittest.TestCase):
    def test_countBits(self):
        test_patterns = [
            (5, [0, 1, 1, 2, 1, 2]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countBits(arg), expected)


if __name__ == '__main__':
    unittest.main()
