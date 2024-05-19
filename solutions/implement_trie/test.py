import unittest
import implement_trie.index as main


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [
            (
                [
                    "apple",
                    ("apple", True),
                    ("app", False),
                    ("app", True),
                    "app",
                    ("app", True),
                ]
            ),
        ]

        s = main.Solution()
        t = s.Trie()
        for i, (arg) in enumerate(test_patterns):
            with self.subTest(test=i):
                t.insert(arg[0])
                self.assertEqual(t.search(arg[1][0]), arg[1][1])
                self.assertEqual(t.search(arg[2][0]), arg[2][1])
                self.assertEqual(t.startsWith(arg[3][0]), arg[3][1])
                t.insert(arg[4])
                self.assertEqual(t.search(arg[5][0]), arg[5][1])


if __name__ == "__main__":
    unittest.main()
