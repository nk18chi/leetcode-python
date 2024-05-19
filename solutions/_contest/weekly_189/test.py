import unittest
import _contest.weekly_189.index as main


class Test(unittest.TestCase):
    def test_peopleIndexes(self):
        test_patterns = [
            (
                [
                    [
                        "arrtztkotazhufrsfczr",
                        "knzgidixqgtnahamebxf",
                        "zibvccaoayyihidztflj",
                    ],
                    ["cffiqfviuwjowkppdajm", "owqvnrhuzwqohquamvsz"],
                    [
                        "knzgidixqgtnahamebxf",
                        "owqvnrhuzwqohquamvsz",
                        "qzeqyrgnbplsrgqnplnl",
                    ],
                    ["arrtztkotazhufrsfczr", "cffiqfviuwjowkppdajm"],
                    [
                        "arrtztkotazhufrsfczr",
                        "knzgidixqgtnahamebxf",
                        "owqvnrhuzwqohquamvsz",
                        "qzeqyrgnbplsrgqnplnl",
                        "zibvccaoayyihidztflj",
                    ],
                ],
                [1, 3, 4],
            ),
            (
                [
                    ["leetcode", "google", "facebook"],
                    ["google", "microsoft"],
                    ["google", "facebook"],
                    ["google"],
                    ["amazon"],
                ],
                [0, 1, 4],
            ),
            (
                [
                    [
                        "nxaqhyoprhlhvhyojanr",
                        "ovqdyfqmlpxapbjwtssm",
                        "qmsbphxzmnvflrwyvxlc",
                        "udfuxjdxkxwqnqvgjjsp",
                        "yawoixzhsdkaaauramvg",
                        "zycidpyopumzgdpamnty",
                    ],
                    [
                        "nxaqhyoprhlhvhyojanr",
                        "ovqdyfqmlpxapbjwtssm",
                        "udfuxjdxkxwqnqvgjjsp",
                        "yawoixzhsdkaaauramvg",
                        "zycidpyopumzgdpamnty",
                    ],
                    [
                        "ovqdyfqmlpxapbjwtssm",
                        "qmsbphxzmnvflrwyvxlc",
                        "udfuxjdxkxwqnqvgjjsp",
                        "yawoixzhsdkaaauramvg",
                        "zycidpyopumzgdpamnty",
                    ],
                ],
                [0],
            ),
        ]

        for i, (arg1, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.peopleIndexes(arg1), expected)

    def test_numPoints(self):
        test_patterns = [
            ([[-2, 0], [2, 0], [0, 2], [0, -2]], 2, 4),
            ([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5, 5),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numPoints(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
