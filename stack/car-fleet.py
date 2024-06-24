# there are n cars travelling to the same destination on a one-lane highway
# you are given two arrays of integers position and speed, both of length n
# position[i] is the position of the ith car (in miles)
# speed[i] is the position of the ith car (in miles per hour)
# the destination is at position target miles
# a car can not pass another car ahead of it
# it can only catch up to another car and then drive at the same speed as the car ahead of it
# a car fleet is a non-empty set of cars driving at the same position and same speed
# a single car is also considered a car fleet
# if a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet
# return the number of different car fleets that will arrive at the destination

# Example 1:
# Input: target = 10, position = [1,4], speed = [3,2]
# Output: 1
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:
# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
# Output: 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        pair.sort()

        for p, s in pair[::-1]:
            arrivalTime = (target - p) / s

            if not stack or arrivalTime > stack[-1]:
                stack.append(arrivalTime)
        
        return len(stack)

# time complexity: O(nlogn) <-- dominated by sorting the input
# space complexity: O(n)