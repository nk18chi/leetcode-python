import unittest
import all_paths_from_source_to_target.index as main


class Test(unittest.TestCase):
    def test_allPathsSourceTarget(self):
        test_patterns = [
            ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.allPathsSourceTarget(arg), expected)


if __name__ == "__main__":
    unittest.main()
