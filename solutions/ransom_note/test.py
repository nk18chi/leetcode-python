import unittest
import solutions.ransom_note.index as main


class Test(unittest.TestCase):
    def test_canConstruct(self):
        test_patterns = [
            ("", "", True),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.canConstruct(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
