import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row 
        for row in board:
            counter = collections.Counter([x for x in row if x != "."]).values()
            if counter and max(counter) > 1:
                return False

        # Check columns
        for column in range(len(board)):
            counter = collections.Counter(
                [
                    board[row][column] 
                    for row in range(len(board)) 
                    if board[row][column] != "."
                ]
            ).values()

            if counter and max(counter) > 1:
                print("column")
                return False

        # Check square
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [
                    board[x][y] 
                    for x in range(i, i + 3) 
                    for y in range(j, j + 3) 
                    if board[x][y] != "."
                ]
                counter = collections.Counter(square).values()
                if counter and max(counter) > 1:
                    print("square")
                    return False
        
        return True