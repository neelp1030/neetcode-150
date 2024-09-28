# you are given a 2D matrix board containing 'X' and 'O' characters
# if a continuous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded
# change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board

# observe that all unsurrounded regions will be connected to the border
# using this, we can determine the unsurrounded regions by running BFS/DFS on all the border 'O' cells, changing them to a temporary value 'T'
# then, the remaining 'O' cells on the board will be the ones to be captured, so we can change all the 'O' cells to 'X'
# lastly, we can change the 'T' cells back to 'O'

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Step 1
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or c == 0 or r == rows - 1 or c == cols - 1):
                    dfs(r, c)
        
        # Step 2
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # Step 3
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

# time complexity: O(n * m)
# space complexity: O(n * m)