# you are given a 2D matrix grid
# each cell can have one of three possible values
# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten
# return the minimum number of minutes that must elapse until there are zero fresh fruits remaining
# if this state is impossible within the grid, return -1

# at the start, we will traverse the entire grid and count up the initial number of fresh fruit
# then, we will initialize a queue with all the rotten fruit
# after that, we will run a multi-source BFS using that queue until it becomes empty or there are zero fresh fruits remaining
# in each iteration of the multi-source BFS, we will increment a timer to keep track of time (initially set to 0)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        time = 0
        remainingFresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    remainingFresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and remainingFresh:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        remainingFresh -= 1
        
            time += 1
        
        return time if not remainingFresh else -1

# time complexity: O(n * m)
# space complexity: O(n * m)