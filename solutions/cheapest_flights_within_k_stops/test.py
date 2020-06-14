import unittest
import solutions.cheapest_flights_within_k_stops.index as main


class Test(unittest.TestCase):
    def test_findCheapestPrice(self):
        test_patterns = [
            (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        ]

        for i, (arg1, arg2, arg3, arg4, arg5, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                # tree: TreeNode = createTreeNode(arg)
                self.assertEqual(s.findCheapestPrice(arg1, arg2, arg3, arg4, arg5), expected)

        # (test) List Node
        # for i, (arg, expected) in enumerate(test_patterns):
        #     with self.subTest(test=i):
        #         s = main.Solution()
        #         ln = createListNode(arg)
        #         ans: ListNode = getValFromListNode(s.functionName(ln))
        #         self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()
