# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        operators: List[str] = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                n1: int = stack.pop()
                n2: int = stack.pop()
                if token == operators[0]:
                    stack.append(n2 + n1)
                elif token == operators[1]:
                    stack.append(n2 - n1)
                elif token == operators[2]:
                    stack.append(n2 * n1)
                elif token == operators[3]:
                    stack.append(int(float(n2) / n1))
            else:
                stack.append(int(token))
        return int(stack[0])
