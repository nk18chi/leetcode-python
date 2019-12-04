import unittest
import importlib
f = importlib.import_module('solutions.136_single_number.index')


class Test(unittest.TestCase):

    def test_singleNumber(self):
        test_patterns = [
            ([2, 2, 1], 1),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.singleNumber(arg), expected)


if __name__ == '__main__':
    unittest.main()
