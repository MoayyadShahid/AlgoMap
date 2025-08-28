class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        '''
        We split this problem into 3 parts: check rows, columns, sub-boxes.
        '''

        # check row
        # We do Row-first search
        for i in range(len(board)):
            # we create a set for each row, and add all nums to that set
            row = set()
            for j in range(len(board[0])):
                # if a num is already in the set, then we have repeated ourselves so this is invalid board
                if board[i][j] in row:
                    return False
                 # we only add a element of the board as long as its a num, so if it isn't a '.'
                elif board[i][j] != '.':
                    row.add(board[i][j])

        # check columns
        for j in range(len(board[0])):
            # we create a set for each col, and add all nums to that set
            col = set()
            for i in range(len(board)):
                # if a num is already in the set, then we have repeated ourselves so this is invalid board
                if board[i][j] in col:
                    return False
                # we only add a element of the board as long as its a num, so if it isn't a '.'
                elif board[i][j] != '.':
                    col.add(board[i][j])
        
        # check 3x3 sub boxes
        # use the top right corner of each sub box as the starting index point
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                # for each new sub-box loop we create a box set
                box = set()
                # now we loop through the sub-boxes themselves
                for di in range(0, 3):
                    for dj in range(0, 3):
                        # we check if the sub-box element exists in the set, if so return false as that board is invalid
                        if board[i + di][j + dj] in box:
                            return False
                        # we only add a element of the board as long as its a num, so if it isn't a '.'
                        elif board[i + di][j + dj] != '.':
                            box.add(board[i + di][j + dj])
        
        return True
        # Run Time: O(N^2), could be argued that this is O(1) since you're guaranteed a 9x9 grid so its O(81) search
