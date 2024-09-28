# you are given a m x n grid initialized with these three possible values:
# 1. -1 - a water cell that cannot be traversed
# 2. 0 - a treasure chest
# 3. INF - a land cell that can be traversed.

# fill each land cell with the distance to its nearest treasure chest
# if a land cell cannot reach a treasure chest, then the value should remain INF
# assume the grid can only be traversed up, down, left, or right

# the distance from a land cell to the nearest treasure chest is the same as the distance from the nearest treasure chest to the land cell
# so we can do a multi-source BFS solution where we simultaneously run BFS on all the treasure chests
# we will initialize our queue to contain all the treasure chests
# then we will pop all the chests and add their adjacent cells, and repeat level by level
# until the queue becomes empty

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        def addCell(r, c):
            if r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] == 2147483647:
                queue.append((r, c))
                grid[r][c] = distance

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        distance = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            distance += 1
        
# time complexity: O(n * m)
# space complexity: O(n * m)