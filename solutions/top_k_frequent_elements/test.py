import unittest
import solutions.top_k_frequent_elements.index as main


class Test(unittest.TestCase):
    def test_topKFrequent(self):
        test_patterns = [
            ([1, 1, 1, 2, 2, 3], 2, [2, 1]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.topKFrequent(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
