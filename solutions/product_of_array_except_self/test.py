import unittest
import solutions.product_of_array_except_self.index as main


class Test(unittest.TestCase):
    def test_productExceptSelf(self):
        test_patterns = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.productExceptSelf(arg), expected)


if __name__ == '__main__':
    unittest.main()
