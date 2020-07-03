import unittest
import solutions.prison_cells_after_n_days.index as main


class Test(unittest.TestCase):
    def test_prisonAfterNDays(self):
        test_patterns = [
            ([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.prisonAfterNDays(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
