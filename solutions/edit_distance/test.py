import unittest
import solutions.edit_distance.index as main


class Test(unittest.TestCase):
    def test_minDistance(self):
        test_patterns = [
            ("", "a", 1),
            ("horse", "ros", 3),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.minDistance(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
