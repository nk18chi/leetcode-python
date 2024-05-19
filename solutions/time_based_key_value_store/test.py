import unittest
import time_based_key_value_store.index as main
from typing import List


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [
            (
                ["TimeMap", "set", "get", "get", "set", "get", "get"],
                [
                    [],
                    ["foo", "bar", 1],
                    ["foo", 1],
                    ["foo", 3],
                    ["foo", "bar2", 4],
                    ["foo", 4],
                    ["foo", 5],
                ],
                [None, None, "bar", "bar", None, "bar2", "bar2"],
            ),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                res: List[str] = []
                timeMap = None
                for j in range(len(arg1)):
                    if arg1[j] == "TimeMap":
                        timeMap = main.Solution().TimeMap()
                        res.append(None)
                    elif arg1[j] == "set":
                        timeMap.set(*arg2[j])
                        res.append(None)
                    elif arg1[j] == "get":
                        res.append(timeMap.get(*arg2[j]))
                self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
