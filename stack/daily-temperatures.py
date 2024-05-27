# you are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day
# return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day
# if there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead

# Example 1:
# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

# Example 2:
# Input: temperatures = [22,21,20]
# Output: [0,0,0]

# this problem uses a monotonically decreasing stack technique, as we pop if our new element is larger than the top of our stack
# but we need to make sure to package the index of the temperature in the stack elements as that info would be lost

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                res[j] = i - j
            
            stack.append((temp, i))
        
        return res

# time complexity: O(n)
# space complexity: O(n)