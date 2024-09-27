# given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands

# an island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water
# you may assume water is surrounding the grid (i.e. all the edges are water)

# we wish to find the number of islands
# we can run bfs/dfs on each cell of the grid one by one
# in each run of the bfs/dfs, we will visit all the connected land cells and mark them as visited
# we will skip running bfs/dfs again on visited cells
# each time we run the bfs/dfs, we will increment numOfIslands by 1
# we skip running bfs/dfs on water cells as well
# we use a set for keeping track of visited cells
# the base case for the dfs will be:
# if i or j are out of bounds
# or if (i, j) has already been visited
# or if grid[i][j] == '0'
# then we simply return

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or (r, c) in visited or grid[r][c] == '0':
                return
            
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                # if the cell has already been visited, or if it is water ('0'), then skip
                if (r, c) in visited or grid[r][c] == '0':
                    continue
                dfs(r, c)
                numOfIslands += 1
        
        return numOfIslands

# time complexity: O(n * m)
# space complexity: O(n * m)