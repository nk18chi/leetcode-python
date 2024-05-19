import unittest
import letter_combinations_of_a_phone_number.index as main


class Test(unittest.TestCase):
    def test_letterCombinations(self):
        test_patterns = [
            ("", []),
            ("2", ["a", "b", "c"]),
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.letterCombinations(arg), expected)


if __name__ == "__main__":
    unittest.main()
