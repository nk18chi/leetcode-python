import fizz_buzz.index as main
import unittest


class Test(unittest.TestCase):
    def test_fizzBuzz(self):
        test_patterns = [
            (
                15,
                [
                    "1",
                    "2",
                    "Fizz",
                    "4",
                    "Buzz",
                    "Fizz",
                    "7",
                    "8",
                    "Fizz",
                    "Buzz",
                    "11",
                    "Fizz",
                    "13",
                    "14",
                    "FizzBuzz",
                ],
            )
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.fizzBuzz(arg), expected)


if __name__ == "__main__":
    unittest.main()
