import unittest

import solutions.shortest_distance_to_a_character.index as main


class Test(unittest.TestCase):

    def test_shortestToChar(self):
        test_patterns = [
            ("loveleetcode", "e", [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.shortestToChar(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
