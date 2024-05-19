import unittest
import contains_duplicate.index as main


class Test(unittest.TestCase):
    def test_containsDuplicate(self):
        test_patterns = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.containsDuplicate(arg), expected)


if __name__ == "__main__":
    unittest.main()
