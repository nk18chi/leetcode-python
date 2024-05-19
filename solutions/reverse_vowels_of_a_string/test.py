import unittest
import reverse_vowels_of_a_string.index as main


class Test(unittest.TestCase):
    def test_reverseVowels(self):
        test_patterns = [("hello", "holle"), ("aA", "Aa")]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.reverseVowels(arg), expected)


if __name__ == "__main__":
    unittest.main()
