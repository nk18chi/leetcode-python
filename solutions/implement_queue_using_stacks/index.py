# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.list.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        i = self.list[0]
        self.list = self.list[1:]

        return i

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.list[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.list) == 0


# Your MyQueue object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    param_2 = obj.peek()
    param_3 = obj.pop()
    param_4 = obj.empty()
