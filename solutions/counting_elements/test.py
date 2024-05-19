import unittest
import counting_elements.index as main


class Test(unittest.TestCase):
    def test_countElements(self):
        test_patterns = [
            ([1, 2, 3], 2),
            ([1, 1, 3, 3, 5, 5, 7, 7], 0),
            ([1, 3, 2, 3, 5, 0], 3),
            ([1, 1, 2, 2], 2),
            ([1, 1, 2], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countElements(arg), expected)


if __name__ == "__main__":
    unittest.main()
