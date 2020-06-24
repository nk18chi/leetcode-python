import unittest
import solutions.unique_binary_search_trees.index as main


class Test(unittest.TestCase):
    def test_numTrees(self):
        test_patterns = [
            (3, 5),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numTrees(arg), expected)


if __name__ == '__main__':
    unittest.main()
