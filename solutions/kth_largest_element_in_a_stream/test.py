import unittest
import solutions.kth_largest_element_in_a_stream.index as main


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [
            (3, [4, 5, 8, 2], [(3, 4), (5, 5), (10, 5), (9, 8), (4, 8)]),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                k = s.KthLargest(arg1, arg2)
                for e in expected:
                    self.assertEqual(k.add(e[0]), e[1])


if __name__ == '__main__':
    unittest.main()
