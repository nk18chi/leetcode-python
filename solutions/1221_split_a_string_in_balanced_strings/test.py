import unittest
import importlib
f = importlib.import_module(
    'solutions.1221_split_a_string_in_balanced_strings.index')


class Test(unittest.TestCase):
    def test_balancedStringSplit(self):
        test_patterns = [
            ("RLRRLLRLRL", 4),
            ("RLRRRLLRLL", 2)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.balancedStringSplit(arg), expected)


if __name__ == '__main__':
    unittest.main()
