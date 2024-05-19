import unittest

import two_city_scheduling.index as main


class Test(unittest.TestCase):
    def test_twoCitySchedCost(self):
        test_patterns = [
            ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
            (
                [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]],
                1859,
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.twoCitySchedCost(arg), expected)


if __name__ == "__main__":
    unittest.main()
