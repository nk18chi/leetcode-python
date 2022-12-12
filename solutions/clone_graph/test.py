import unittest
import solutions.clone_graph.index as main
from solutions._class.node import Node, createDoublyNeighborNode, getFlattenNeighborNode


class Test(unittest.TestCase):
    def test_cloneGraph(self):
        test_patterns = [
            ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                node: Node = createDoublyNeighborNode(arg)
                self.assertEqual(getFlattenNeighborNode(s.cloneGraph(node)), expected)


if __name__ == '__main__':
    unittest.main()
