import unittest
import importlib
f = importlib.import_module('solutions.476_number_complement.index')


class Test(unittest.TestCase):
    def test_findComplement(self):
        test_patterns = [
            (5, 2),
            (1, 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.findComplement(arg), expected)


if __name__ == '__main__':
    unittest.main()
