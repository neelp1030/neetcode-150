# you are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c)
# the islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides
# water can flow in four directions (up, down, left, or right) from a cell to a neighbouring cell with height equal or lower
# water can also flow into the ocean from cells adjacent to the ocean
# find all cells where water can flow from that cell to both the Pacific and Atlantic Oceans
# return it as a 2D list where each element is a list [r, c] representing the row and column of the cell
# you may return the answer in any order

# similar idea to previous problems
# let's go in the opposite direction
# we start at Atlantic and Pacific Ocean respectively, and run DFS from those initial cells to populate the visited sets
# the visited sets will be separate for Atlantic and Pacific respectively
# since we're going in the opposite direction, we can only flow to the new cell if valNew >= valPrev
# at the end, we will create the final result list based on the contents of the two visited sets

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        pacificVisited = set()
        atlanticVisited = set()

        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or heights[r][c] < prev:
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        # the initial cells corresponding to the oceans will all be on the border of the grid, so let's traverse them
        for r in range(rows):
            dfs(r, 0, pacificVisited, 0)
            dfs(r, cols - 1, atlanticVisited, 0)
        
        for c in range(cols):
            dfs(0, c, pacificVisited, 0)
            dfs(rows - 1, c, atlanticVisited, 0)

        res = []

        for r, c in pacificVisited:
            if (r, c) in atlanticVisited:
                res.append([r, c])
        
        return res

# time complexity: O(n * m)
# space complexity: O(n * m)