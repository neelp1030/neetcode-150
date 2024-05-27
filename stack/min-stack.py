# design a stack class that supports the push, pop, top, and getMin operations
# MinStack() initializes the stack object
# void push(int val) pushes the element val onto the stack
# void pop() removes the element on the top of the stack
# int top() gets the top element of the stack
# int getMin() retrieves the minimum element in the stack
# each function should run in O(1) time

# Example 1:
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
# Output: [null,null,null,null,0,null,2,1]
# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1

# the implementation will use two stacks
# one standard stack (which contains the actual inserted elements in LIFO order)
# one min stack (which will contain the corresponding minimum element in the standard stack at each insertion point)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# time complexity: O(1)
# space complexity: O(n)