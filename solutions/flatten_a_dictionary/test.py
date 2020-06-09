import unittest
import solutions.flatten_a_dictionary.index as main


class Test(unittest.TestCase):
    def test_flatten_dictionary(self):
        test_patterns = [
            ({
                "Key1": "1",
                "Key2": {
                    "a": "2",
                    "b": "3",
                    "c": {
                        "d": "3",
                        "e": {
                            "": "1"
                        }
                    }
                }
            },
                {
                "Key1": "1",
                "Key2.a": "2",
                "Key2.b": "3",
                "Key2.c.d": "3",
                "Key2.c.e": "1"
            }),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.flatten_dictionary(arg), expected)


if __name__ == '__main__':
    unittest.main()
