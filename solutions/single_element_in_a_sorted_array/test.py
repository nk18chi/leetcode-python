import unittest
import solutions.single_element_in_a_sorted_array.index as main


class Test(unittest.TestCase):
    def test_singleNonDuplicate(self):
        test_patterns = [
            ([1, 1, 2, 2, 3, 3, 4, 4, 5], 5),
            ([1, 1, 2, 3, 3, 4, 4, 5, 5], 2),

        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.singleNonDuplicate(arg), expected)


if __name__ == '__main__':
    unittest.main()
