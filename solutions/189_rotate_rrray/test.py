import unittest
import importlib
f = importlib.import_module('solutions.189_rotate_rrray.index')


class Test(unittest.TestCase):

    def test_rotate(self):
        test_patterns = [
            ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.rotate(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
