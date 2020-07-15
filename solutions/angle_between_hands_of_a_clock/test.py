import unittest
import solutions.angle_between_hands_of_a_clock.index as main


class Test(unittest.TestCase):
    def test_angleClock(self):
        test_patterns = [
            (12, 30, 165.00000),
            (1, 57, 76.50000),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.angleClock(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
