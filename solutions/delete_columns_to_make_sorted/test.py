import unittest
import solutions.delete_columns_to_make_sorted.index as main


class Test(unittest.TestCase):
    def test_minDeletionSize(self):
        test_patterns = [
            (["cba", "daf", "ghi"], 1),
            (["abcdef", "uvwxyz"], 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minDeletionSize(arg), expected)


if __name__ == '__main__':
    unittest.main()
