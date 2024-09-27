# you are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land)
# an island is defined as a group of 1's connected horizontally or vertically
# you may assume all four edges of the grid are surrounded by water
# the area of an island is defined as the number of cells within the island
# return the maximum area of an island in grid
# if no island exists, return 0

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c) -> int:
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            res = 1

            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            
            return res

        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea

# time complexity: O(n * m)
# space complexity: O(n * m)