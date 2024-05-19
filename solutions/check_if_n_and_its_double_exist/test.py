import unittest
import check_if_n_and_its_double_exist.index as main


class Test(unittest.TestCase):
    def test_checkIfExist(self):
        test_patterns = [
            ([10, 2, 5, 3], True),
            ([-2, 0, 10, -19, 4, 6, -8], False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.checkIfExist(arg), expected)


if __name__ == "__main__":
    unittest.main()
