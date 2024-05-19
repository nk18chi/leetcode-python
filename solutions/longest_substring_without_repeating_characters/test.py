import unittest
import longest_substring_without_repeating_characters.index as main
from _class.list_node import ListNode, createListNode, getListNode


class Test(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        test_patterns = [("abcbabcd", 4), ("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                ans: ListNode = s.lengthOfLongestSubstring(arg1)
                self.assertEqual(ans, expected)


if __name__ == "__main__":
    unittest.main()
