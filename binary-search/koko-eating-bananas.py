# you are given an integer array piles where piles[i] is the number of bananas in the ith pile
# you are also given an integer h, which represents the number of hours you have to eat all the bananas
# you may decide your bananas-per-hour eating rate of k
# each hour, you may choose a pile of bananas and eat k bananas from that pile
# if the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour
# return the minimum integer k such that you can eat all the bananas within h hours

# Example 1:
# Input: piles = [1,4,3,2], h = 9
# Output: 2
# Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

# Example 2:
# Input: piles = [25,10,23,4], h = 4
# Output: 25

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

# time complexity: O(log(max(p)) * len(p))
# space complexity: O(1)