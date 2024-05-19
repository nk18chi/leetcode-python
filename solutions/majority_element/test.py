import unittest
import majority_element.index as main


class Test(unittest.TestCase):
    def test_majorityElement(self):
        test_patterns = [
            ([2, 2, 1, 1, 1, 2, 2], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.majorityElement(arg), expected)


if __name__ == "__main__":
    unittest.main()
