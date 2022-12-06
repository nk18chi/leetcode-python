import unittest
import solutions.count_and_say.index as main


class Test(unittest.TestCase):
    def test_countAndSay(self):
        test_patterns = [
            (1, '1'),
            (4, '1211'),
            (5, '111221'),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.countAndSay(arg), expected)


if __name__ == '__main__':
    unittest.main()
