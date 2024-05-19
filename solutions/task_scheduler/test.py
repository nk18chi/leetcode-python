import unittest
import task_scheduler.index as main


class Test(unittest.TestCase):
    def test_leastInterval(self):
        test_patterns = [
            (["A", "A", "A", "B", "B", "B"], 2, 8),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.leastInterval(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
