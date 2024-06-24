# you are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation
# return the integer that represents the evaluation of the expression
# the operands may be integers or the results of other operations
# the operators include +, -, *, and /
# assume that division between integers always truncates toward zero

# Example 1:
# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(float(first) / second))
            else:
                stack.append(int(t))
        
        return stack[0]

# time complexity: O(n)
# space complexity: O(n)