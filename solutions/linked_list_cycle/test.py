import unittest
import linked_list_cycle.index as main


class Test(unittest.TestCase):
    def test_hasCycle(self):
        test_patterns = [
            ([2, 7, 11, 15], False),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                n = main.createListNode(arg)
                self.assertEqual(s.hasCycle(n), expected)


if __name__ == "__main__":
    unittest.main()
