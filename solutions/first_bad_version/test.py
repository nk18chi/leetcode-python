import unittest
import first_bad_version.index as main


class Test(unittest.TestCase):
    def test_firstBadVersion(self):
        test_patterns = [
            (5, 4),
            (2126753390, 1702766719),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                main.answer = expected
                self.assertEqual(s.firstBadVersion(arg), expected)


if __name__ == "__main__":
    unittest.main()
