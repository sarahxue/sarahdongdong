class MinStack:
    # use 2 stacks, one for min val, so getMin has o(1) time
    # each push or pop also update minStack
    # all ops time O(1) space O(n)

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # get min between new val 
        val = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
