# you are given a 9 x 9 sudoku board
# a sudoku board is valid if the following rules are followed
# each row must contain the digits 1-9 without repetition
# each column must contain the digits 1-9 without repetition
# each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition
# return true if the sudoku board is valid, otherwise return false
# note: a board does not need to be full or be solvable to be valid (we just need to check that there are no existing duplicates)

# we abuse hashsets to solve this problem
# we know that the board is 9 x 9
# the core idea of this problem is to minimize redundancy in visiting the individual cells of the board
# we can create all the hashsets we need to ensure the validity of the board
# but we only need to traverse the 9 x 9 board once (one pass), and in each traversal we may be updating several hashsets at a time
# so how many hashsets do we need?
# we need to check for each row, so 9 rows
# we need to check for each column, so 9 columns
# we need to check for each 3 x 3 sub-boxes, so 9 sub-boxes
# instead of creating 27 separate variables for each of the hashsets, we can condense it a bit better
# for the 9 rows hashsets, we can use a hashmap with the key being the row number (0 to 8)
# similarly ^ for the 9 columns hashsets
# for the 9 sub-boxes hashsets, we can use a hashmap with the key being a tuple (x, y) where x and y both range between 0 and 2, this will allow us to uniquely determine the sub-box
# each cell will belong to 1 row, 1 column, and 1 sub-box!

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_sets_map = collections.defaultdict(set)
        cols_sets_map = collections.defaultdict(set)
        boxes_sets_map = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                box_x = i // 3
                box_y = j // 3

                if board[i][j] in rows_sets_map[i] or board[i][j] in cols_sets_map[j] or board[i][j] in boxes_sets_map[(box_x, box_y)]:
                    return False
                
                rows_sets_map[i].add(board[i][j])
                cols_sets_map[j].add(board[i][j])
                boxes_sets_map[(box_x, box_y)].add(board[i][j])
        
        return True

# time complexity: O(1)
# space complexity: O(1)
# ^ since board is fixed size