import unittest
import importlib
f = importlib.import_module('solutions.705_design_hashSet.index')


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [([[1],
                           [1, 2],
                           True,
                           False,
                           [1, 2],
                           True,
                           [1],
                           False]),
                         ]

        for i, expected in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.MyHashSet()
                s.add(1)
                self.assertEqual(s.print(), expected[0])
                s.add(2)
                self.assertEqual(s.print(), expected[1])
                self.assertEqual(s.contains(1), expected[2])
                self.assertEqual(s.contains(3), expected[3])
                s.add(2)
                self.assertEqual(s.print(), expected[4])
                self.assertEqual(s.contains(2), expected[5])
                s.remove(2)
                self.assertEqual(s.print(), expected[6])
                self.assertEqual(s.contains(2), expected[7])


if __name__ == '__main__':
    unittest.main()
