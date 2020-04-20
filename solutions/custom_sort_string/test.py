import unittest
import solutions.custom_sort_string.index as main


class Test(unittest.TestCase):
    def test_customSortString(self):
        test_patterns = [
            ("kqep", "pekeq", "kqeep"),
            ("cba", "abcd", "dcba"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.customSortString(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
