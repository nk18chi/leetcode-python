import unittest
import maximum_number_of_balloons.index as main


class Test(unittest.TestCase):
    def test_maxNumberOfBalloons(self):
        test_patterns = [
            ("loonbalxballpoon", 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxNumberOfBalloons(arg), expected)


if __name__ == "__main__":
    unittest.main()
