import unittest
import solutions.number_of_1_bits.index as main


class Test(unittest.TestCase):
    def test_hammingWeight(self):
        test_patterns = [
            (11, 3),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.hammingWeight(arg), expected)


if __name__ == '__main__':
    unittest.main()
