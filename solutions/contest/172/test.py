import unittest
import importlib
f = importlib.import_module('solutions.contest.172.index')


class Test(unittest.TestCase):
    def test_maximum69Number(self):
        test_patterns = [
            (9996, 9999),
            (9669, 9969),
            (9999, 9999)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.maximum69Number(arg), expected)

    def test_printVertically(self):
        test_patterns = [
            ("TO BE OR NOT TO BE", [
                "TBONTB", "OEROOE", "   T"]), ("HOW ARE YOU", [
                    "HAY", "ORO", "WEU"]), ("CONTEST IS COMING", [
                        "CIC", "OSO", "N M", "T I", "E N", "S G", "T"])]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.printVertically(arg), expected)

    # def test_removeLeafNodes(self):
    #     test_patterns = [
    #         (2, [1, None, 3, None, 4]),
    #     ]

    #     for i, (arg, expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = f.Solution()
    #             tree = f.createTreeNode([1, 2, 3, 2, 2, 2, 4])
    #             self.assertEqual(s.removeLeafNodes(tree, arg), expected)

    # def test_minTaps(self):
    #     test_patterns = [
    #         (7, [1, 2, 1, 0, 2, 1, 0, 1], 3),
    #         (5, [3, 4, 1, 1, 0, 0], 1),
    #     ]

    #     for i, (arg1, arg2, expected) in enumerate(test_patterns):
    #         with self.subTest(test=i):
    #             s = f.Solution()
    #             self.assertEqual(s.minTaps(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
