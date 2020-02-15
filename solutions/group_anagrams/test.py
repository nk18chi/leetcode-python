import unittest
import solutions.group_anagrams.index as main


class Test(unittest.TestCase):
    def test_groupAnagrams(self):
        test_patterns = [
            (["eat", "tea", "tan", "ate", "nat", "bat"], [
                ['eat', 'tea', 'ate'],
                ['tan', 'nat'],
                ["bat"]
            ]
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.groupAnagrams(arg), expected)


if __name__ == '__main__':
    unittest.main()
