import unittest

import jewels_and_stones.index as main


class Test(unittest.TestCase):
    def test_numJewelsInStones(self):
        test_patterns = [
            ("aA", "aAAbbbb", 3),
            ("z", "ZZ", 0),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numJewelsInStones(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
