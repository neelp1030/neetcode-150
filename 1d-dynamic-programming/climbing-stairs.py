# you are given an integer n representing the number of steps to reach the top of a staircase
# you can climb with either 1 or 2 steps at a time
# return the number of distinct ways to climb to the top of the staircase

# bottom-up approach: f(n) = 1, f(n - 1) = 1, work your way backwards to f(0) where f(x) = f(x + 1) + f(x + 2)

class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 1

        # we want to run n - 1 times
        for i in range(n - 1):
            temp = n1 + n2
            n2 = n1
            n1 = temp
        
        return n1