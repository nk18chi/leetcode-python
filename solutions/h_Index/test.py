import unittest
import h_Index.index as main


class Test(unittest.TestCase):
    def test_hIndex(self):
        test_patterns = [
            ([3, 0, 6, 1, 5], 3),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.hIndex(arg), expected)


if __name__ == "__main__":
    unittest.main()
