import unittest
import solutions.find_smallest_letter_greater_than_target.index as main


class Test(unittest.TestCase):
    def test_nextGreatestLetter(self):
        test_patterns = [
            (["c", "f", "j"], "j", "c"),
            (["c", "f", "j"], "k", "c"),
            (["c", "f", "j"], "d", "f"),
            (["c", "f", "j"], "a", "c"),
            (["c", "f", "j"], "c", "f"),
            (["c", "f", "j"], "g", "j"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.nextGreatestLetter(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
