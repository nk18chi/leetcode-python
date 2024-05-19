import unittest
import flatten_a_multilevel_doubly_linked_list.index as main

from _class.node import Node, createDoublyNode, getFlattenDoublyNode


class Test(unittest.TestCase):
    def test_flatten(self):
        test_patterns = [
            (
                [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12],
                [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6],
            ),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                node: Node = createDoublyNode(arg)
                self.assertEqual(
                    getFlattenDoublyNode(s.flatten(node)),
                    getFlattenDoublyNode(createDoublyNode(expected)),
                )


if __name__ == "__main__":
    unittest.main()
