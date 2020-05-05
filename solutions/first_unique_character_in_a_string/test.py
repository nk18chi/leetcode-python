import unittest
import solutions.first_unique_character_in_a_string.index as main


class Test(unittest.TestCase):
    def test_firstUniqChar(self):
        test_patterns = [
            ("leetcode", 0),
            ("loveleetcode", 2)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.firstUniqChar(arg), expected)


if __name__ == '__main__':
    unittest.main()
