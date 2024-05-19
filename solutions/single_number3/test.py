import unittest
import single_number3.index as main


class Test(unittest.TestCase):
    def test_singleNumber(self):
        test_patterns = [
            ([1, 2, 1, 3, 2, 5], [3, 5]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.singleNumber(arg), expected)


if __name__ == "__main__":
    unittest.main()
