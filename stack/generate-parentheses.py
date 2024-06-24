# you are given an integer n
# return all well-formed parentheses strings that you can generate with n pairs of parentheses

# Example 1:
# Input: n = 1
# Output: ["()"]

# Example 2:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# we can use a physical stack + an implicit stack (using recursion) to solve this problem
# the physical stack represents our current parenthesis string, while the implicit stack allows us to explore the different paths of the decision tree

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return
            
            if opened < n:
                stack.append('(')
                backtrack(opened + 1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(')')
                backtrack(opened, closed + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res

# time complexity: too complex
# space complexity: O(n)