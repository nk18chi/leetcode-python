import unittest
import fibonacci_number.index as main


class Test(unittest.TestCase):
    def test_fib(self):
        test_patterns = [
            (1, 1),
            (2, 1),
            (4, 3),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.fib(arg), expected)


if __name__ == "__main__":
    unittest.main()
