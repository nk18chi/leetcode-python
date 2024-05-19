import unittest
import permutation_in_string.index as main


class Test(unittest.TestCase):
    def test_checkInclusion(self):
        test_patterns = [
            ("adc", "dcda", True),
            ("ab", "eidbaooo", True),
            ("a", "ab", True),
            ("ab", "eidboaoo", False),
            ("ab", "ab", True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.checkInclusion(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
