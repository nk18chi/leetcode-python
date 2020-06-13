import unittest
import solutions.insert_delete_getRandom.index as main


class Test(unittest.TestCase):
    def test_randomized_set(self):
        test_patterns = [
            ((1, True), (2, False), (2, True), (1, True), (2, False)),
        ]

        for i, (arg1, arg2, arg3, arg4, arg5) in enumerate(test_patterns):
            with self.subTest(test=i):
                r = main.Solution().RandomizedSet()
                self.assertEqual(r.insert(arg1[0]), arg1[1])
                self.assertEqual(r.remove(arg2[0]), arg2[1])
                self.assertEqual(r.insert(arg3[0]), arg3[1])
                self.assertEqual(r.remove(arg4[0]), arg4[1])
                self.assertEqual(r.insert(arg5[0]), arg5[1])


if __name__ == '__main__':
    unittest.main()
