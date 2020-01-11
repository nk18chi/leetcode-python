import unittest
import importlib
f = importlib.import_module('solutions.1137_n_th_tribonacci_number.index')


class Test(unittest.TestCase):
    def test_tribonacci(self):
        test_patterns = [
            (4, 4),
            (25, 1389537)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.tribonacci(arg), expected)


if __name__ == '__main__':
    unittest.main()
