import unittest
import importlib
f = importlib.import_module('solutions.format.index')


class Test(unittest.TestCase):

    def test_functionName(self):
        test_patterns = [
            ([2, 7, 11, 15], 9),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                # tree = f.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.functionName(arg), expected)


if __name__ == '__main__':
    unittest.main()
