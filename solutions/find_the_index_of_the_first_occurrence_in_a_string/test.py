import unittest
import find_the_index_of_the_first_occurrence_in_a_string.index as main


class Test(unittest.TestCase):
    def test_strStr(self):
        test_patterns = [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1)]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.strStr(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
