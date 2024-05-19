import unittest
import reverse_bits.index as main


class Test(unittest.TestCase):
    def test_reverseBits(self):
        test_patterns = [
            (43261596, 964176192),
            (4294967293, 3221225471),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.reverseBits(arg), expected)


if __name__ == "__main__":
    unittest.main()
