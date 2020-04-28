import unittest
import solutions.first_unique_number.index as main


class Test(unittest.TestCase):
    def test_first_unique(self):
        test_patterns = [
            ([2, 3, 5], [2, 5, 2, 2, 3, 3, -1]),
        ]

        for i, (init, value) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                fu = s.FirstUnique(init)
                self.assertEqual(fu.showFirstUnique(), value[0])
                fu.add(value[1])
                self.assertEqual(fu.showFirstUnique(), value[2])
                fu.add(value[3])
                self.assertEqual(fu.showFirstUnique(), value[4])
                fu.add(value[5])
                self.assertEqual(fu.showFirstUnique(), value[6])


if __name__ == '__main__':
    unittest.main()
