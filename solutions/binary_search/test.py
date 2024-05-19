import unittest
import binary_search.index as main


class Test(unittest.TestCase):
    def test_search(self):
        test_patterns = [
            ([2, 7, 11, 15], 9, -1),
            ([-1, 0, 3, 5, 9, 12], 9, 4),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.search(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
