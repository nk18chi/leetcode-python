import unittest
import solutions.queue_reconstruction_by_height.index as main


class Test(unittest.TestCase):
    def test_reconstructQueue(self):
        test_patterns = [
            ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.reconstructQueue(arg), expected)


if __name__ == '__main__':
    unittest.main()
