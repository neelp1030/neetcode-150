# you are given an m x n 2D integer array matrix and an integer target
# each row in matrix is sorted in increasing order
# the first integer of every row is greater than the last integer of the previous row
# return true if target exists within matrix or false otherwise
# can you write a solution that runs in O(log(m * n)) time?

# Example 1:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# Output: true

# Example 2:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
# Output: false

# we can do a two-part binary search for this problem
# first, we will do a binary search to determine which row of the matrix our target belongs in (if any)
# second, we will do a binary search on that row to find our target (if it exists)
# if l > r at the end of the first binary search, that means we weren't able to find a sufficient row, so we return false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # first binary search to find the row containing our target
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        
        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
            
        return False

# time complexity: O(log(m * n))
# space complexity: O(1)