import unittest
import solutions.majority_element.index as main


class Test(unittest.TestCase):
    def test_majorityElement(self):
        test_patterns = [
            ([2, 7, 11, 15], 0),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.majorityElement(arg), expected)


if __name__ == '__main__':
    unittest.main()
