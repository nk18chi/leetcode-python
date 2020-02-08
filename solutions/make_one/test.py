import unittest
import solutions.make_one.index as main


class Test(unittest.TestCase):
    def test_make_one(self):
        test_patterns = [
            (51, 6),
            (1353, 10),
            (2, 1),
            (10, 3),
            (16, 4),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree = main.createTreeNode([5, 5, 5, 1, 1, 5])
                self.assertEqual(s.make_one(arg), expected)


if __name__ == '__main__':
    unittest.main()
