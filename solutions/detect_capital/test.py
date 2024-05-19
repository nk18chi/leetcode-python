import unittest
import detect_capital.index as main


class Test(unittest.TestCase):
    def test_detectCapitalUse(self):
        test_patterns = [
            ("USA", True),
            ("Usa", True),
            ("usa", True),
            ("uSa", False),
            ("FlaG", False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.detectCapitalUse(arg), expected)


if __name__ == "__main__":
    unittest.main()
