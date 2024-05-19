import unittest
import two_sum_5_input_is_a_bst.index as main


class Test(unittest.TestCase):
    def test_findTarget(self):
        test_patterns = [
            ([5, 3, 7, 2, 4, 6, 8], 5, True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                tree = main.createTreeNode(arg1)
                self.assertEqual(s.findTarget(tree, arg2), expected)


if __name__ == "__main__":
    unittest.main()
