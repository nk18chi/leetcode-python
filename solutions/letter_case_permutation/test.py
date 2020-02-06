import unittest

import solutions.letter_case_permutation.index as main


class Test(unittest.TestCase):
    def test_letterCasePermutation(self):
        test_patterns = [
            ("a1b2", ['a1b2', 'A1b2', 'a1B2', 'A1B2'])
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.letterCasePermutation(arg), expected)


if __name__ == '__main__':
    unittest.main()
