import unittest
import binary_number_with_alternating_bits.index as main


class Test(unittest.TestCase):
    def test_hasAlternatingBits(self):
        test_patterns = [
            (5, True),
            (7, False),
            (11, False),
            (10, True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.hasAlternatingBits(arg), expected)


if __name__ == "__main__":
    unittest.main()
