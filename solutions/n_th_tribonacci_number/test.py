import unittest

import solutions.n_th_tribonacci_number.index as main


class Test(unittest.TestCase):
    def test_tribonacci(self):
        test_patterns = [
            (4, 4),
            (25, 1389537)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.tribonacci(arg), expected)


if __name__ == '__main__':
    unittest.main()
