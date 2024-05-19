import unittest
import happy_number.index as main


class Test(unittest.TestCase):
    def test_isHappy(self):
        test_patterns = [
            (19, True),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.isHappy(arg), expected)


if __name__ == "__main__":
    unittest.main()
