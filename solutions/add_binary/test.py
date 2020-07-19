import unittest
import solutions.add_binary.index as main


class Test(unittest.TestCase):
    def test_addBinary(self):
        test_patterns = [
            ("11", "1", "100"),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.addBinary(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
