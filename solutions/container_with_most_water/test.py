import unittest
import container_with_most_water.index as main


class Test(unittest.TestCase):
    def test_maxArea(self):
        test_patterns = [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxArea(arg), expected)


if __name__ == "__main__":
    unittest.main()
