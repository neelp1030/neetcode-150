# you are given a string s consisting of the following characters: (, ), {, }, [, and ]
# the input string s is valid if and only if:
# 1. every open bracket is closed by the same type of close bracket
# 2. open brackets are closed in the correct order
# 3. every close bracket has a corresponding open bracket of the same type
# return true if s is a valid string, and false otherwise

# Example 1:
# Input: s = "[]"
# Output: true

# Example 2:
# Input: s = "([{}])"
# Output: true

# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.

# this is a very basic application of a stack technique
# we will use a fixed size hashmap to associate the open and close brackets of the same kind

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = { ')': '(', ']': '[', '}': '{' }

        for c in s:
            if c in bracketMap:
                if not stack or (stack[-1] != bracketMap[c]):
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack

# time complexity: O(n)
# space complexity: O(1)
