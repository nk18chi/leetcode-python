import unittest
import solutions.lru_cache.index as main


class Test(unittest.TestCase):
    def test_lru_cache(self):
        test_patterns = [
            (2),
        ]

        for i, (arg) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                lrc = s.LRUCache(arg)
                # lrc.put(1, 1)
                # lrc.put(2, 2)
                # self.assertEqual(lrc.get(1), 1)
                # lrc.put(3, 3)
                # self.assertEqual(lrc.get(2), -1)
                # lrc.put(4, 4)
                # self.assertEqual(lrc.get(1), -1)
                # self.assertEqual(lrc.get(3), 3)
                # self.assertEqual(lrc.get(4), 4)

                self.assertEqual(lrc.get(2), -1)
                lrc.put(2, 1)
                lrc.put(1, 1)
                lrc.put(2, 3)
                lrc.put(4, 1)
                self.assertEqual(lrc.get(1), -1)
                self.assertEqual(lrc.get(2), 3)


if __name__ == '__main__':
    unittest.main()
