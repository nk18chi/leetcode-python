import unittest

import number_complement.index as main


class Test(unittest.TestCase):
    def test_findComplement(self):
        test_patterns = [
            (5, 2),
            (1, 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findComplement(arg), expected)


if __name__ == "__main__":
    unittest.main()
