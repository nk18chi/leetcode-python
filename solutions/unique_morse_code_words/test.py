import unittest
import solutions.unique_morse_code_words.index as main


class Test(unittest.TestCase):
    def test_uniqueMorseRepresentations(self):
        test_patterns = [
            (["gin", "zen", "gig", "msg"], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.uniqueMorseRepresentations(arg), expected)


if __name__ == '__main__':
    unittest.main()
