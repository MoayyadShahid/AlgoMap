class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        '''
            The idea is as follows, we need to have 'boundary walls' that we loop over and add to the final 
            array 'spiral'. We need to define certain variables before hand, like 'm' and 'n' to denote the 
            number of rows and columns respectively. Next we need an array 'spiral'. Lastly we need indexes 'i' and 'j' that
            we will update to access the elements of the matrix in a spiral manner.
        
        '''
        m, n = len(matrix), len(matrix[0])
        spiral = []
        i, j = 0, 0

        # we define these constants to serve as constants to indicate which way we are moving in the spiral
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        direction = RIGHT # set the current direction for the spiral

        # we define the initial wall boundaries
        UP_WALL = 0 # the upper wall is the 0th row
        RIGHT_WALL = n # the right wall is at the n'th column so we include the n-1 index column of the matrix
        DOWN_WALL = m # the lower wall is at the m'th row so we include the m-1 index row of the matrix
        LEFT_WALL = -1 # the left wall is defined as -1 to entertain the 0th index column of the matrix

        # now we know we continuously loop until the spiral array has as many elements as in the matrix array (m * n elements)
        while len(spiral) != m*n:
            # we have a case by case basis checking each direction
            # the general strategy is that we use the indexes 'i' and 'j' to access the elements of the matrix within the wall boundaries
            # in each case we update 1 of the index and once we are done we update the wall, indices and the direction for the next loop
            if direction == RIGHT: 
                while j < RIGHT_WALL:
                    spiral.append(matrix[i][j])
                    j += 1
                RIGHT_WALL -= 1
                i += 1
                j -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    spiral.append(matrix[i][j])
                    i += 1
                DOWN_WALL -= 1
                i -= 1
                j -= 1  
                direction = LEFT      
            elif direction == LEFT:
                while j > LEFT_WALL:
                    spiral.append(matrix[i][j])
                    j -= 1
                LEFT_WALL += 1
                i -= 1
                j += 1
                direction = UP
            else:
                while i > UP_WALL:
                    spiral.append(matrix[i][j])
                    i -= 1
                UP_WALL += 1
                i += 1
                j += 1
                direction = RIGHT
        # at the end of it we return the matrix
        return spiral
        # Run Time: O(m * n)
