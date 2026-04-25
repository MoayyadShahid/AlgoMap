class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # outer scope variable to track if we found a valid chain inside the character board
        res = False

        # we need to track 3 items while backtracking, first is the index i of the word that we are processing
        # and then the x and y coordinate of the grid element we are on, if we found a valid character that matches i
        # then we mark it as used via the '#' character (could be any non alphabetical character)
        def backtrack(i, x, y):
            nonlocal res
            # if we were able to backtrack to the length of the word, then we found all relevant characters of the 
            # word in a proper chain in the board
            if i == len(word):
                res = True
                return
            
            # we will only continue backtracking on a word if the current character on the board we are considering 
            # is equal to the current letter in the word
            if board[x][y] == word[i]:
                sol.append(board[x][y])
                # mark the current letter as used
                board[x][y] = "#"
                if x - 1 >= 0:
                    backtrack(i + 1, x - 1, y)
                if x + 1 < len(board):
                    backtrack(i + 1, x + 1, y)
                if y - 1 >= 0:
                    backtrack(i + 1, x, y - 1)
                if y + 1 < len(board[0]):
                    backtrack(i + 1, x, y + 1)
                # we add back the word to the board
                board[x][y] = sol.pop()
                
        # we want to find candidate starting positions for the board by seeing if the letter on the board equals the starting letter
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    backtrack(0, i, j)
        return res
        
    # Run Time: O(m * n * 3 ^ L) , where m * n is traversal of the entire board, and 3 ^ L is the recursive backtracking
