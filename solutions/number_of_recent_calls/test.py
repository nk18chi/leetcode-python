import unittest
import number_of_recent_calls.index as main


class Test(unittest.TestCase):
    def test_recentcounter(self):
        test_patterns = [
            (1, 1),
            (100, 2),
            (3001, 3),
            (3002, 3),
        ]
        s = main.Solution()
        r = s.RecentCounter()
        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                self.assertEqual(r.ping(arg), expected)


if __name__ == "__main__":
    unittest.main()
