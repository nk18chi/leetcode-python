import unittest
import solutions.sort_characters_by_frequency.index as main


class Test(unittest.TestCase):
    def test_frequencySort(self):
        test_patterns = [
            ("tree", "eetr"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.frequencySort(arg), expected)


if __name__ == '__main__':
    unittest.main()
