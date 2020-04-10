import unittest
import solutions.min_stack.index as main


class Test(unittest.TestCase):
    def test_functionName(self):
        test_patterns = [
            (-3, 0, -2),
        ]

        for i, (arg1, arg2, arg3) in enumerate(test_patterns):
            with self.subTest(test=i):
                minStack = main.MinStack()
                minStack.push(-2)
                minStack.push(0)
                minStack.push(-3)
                self.assertEqual(minStack.getMin(), arg1)
                minStack.pop()
                self.assertEqual(minStack.top(), arg2)
                self.assertEqual(minStack.getMin(), arg3)


if __name__ == '__main__':
    unittest.main()
