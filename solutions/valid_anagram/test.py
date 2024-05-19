import unittest
import valid_anagram.index as main


class Test(unittest.TestCase):
    def test_isAnagram(self):
        test_patterns = [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isAnagram(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
