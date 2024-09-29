# you are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase
# after paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor
# you may choose to start at the index 0 or the index 1 floor
# return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost

# bottom-up-approach: let n represent len(cost), then f(n) = 0, f(n - 1) = cost[n - 1], and then work our way backwards to f(0) where f(x) = cost[x] + min(f(x + 1), f(x + 2))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        n1 = cost[n - 1]
        n2 = 0

        for i in range(n - 2, -1, -1):
            temp = cost[i] + min(n1, n2)
            n2 = n1
            n1 = temp
        
        return min(n1, n2)