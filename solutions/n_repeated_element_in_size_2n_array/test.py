import unittest
import solutions.n_repeated_element_in_size_2n_array.index as main


class Test(unittest.TestCase):
    def test_repeatedNTimes(self):
        test_patterns = [
            ([1, 2, 3, 3], 3),
            ([2, 1, 2, 5, 3, 2], 2),
            ([5, 1, 5, 2, 5, 3, 5, 4], 5),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.repeatedNTimes(arg), expected)


if __name__ == '__main__':
    unittest.main()
