import unittest
import importlib
f = importlib.import_module(
    'solutions.1237_find_positive_integer_solution_for_a_given_equation.index')


class CustomFunction:
    def f(self, x, y):
        return x + y


class Test(unittest.TestCase):

    def test_findSolution(self):
        test_patterns = [
            (5, [[1, 4], [2, 3], [3, 2], [4, 1]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                c = CustomFunction()
                self.assertEqual(s.findSolution(c, arg), expected)


if __name__ == '__main__':
    unittest.main()
