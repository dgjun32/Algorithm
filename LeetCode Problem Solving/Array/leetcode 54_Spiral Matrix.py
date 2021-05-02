# Given an m x n matrix, return all elements of the matrix in spiral order.

# Sol 1. Straight forward solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        else:
            ans = []
            i = j = 0
            def up(i,j):
                return i-1, j
            def down(i,j):
                return i+1, j
            def left(i,j):
                return i, j-1
            def right(i,j):
                return i, j+1
            while True:
                #right
                while j < n and matrix[i][j] != 'n':
                    ans.append(matrix[i][j])
                    matrix[i][j] = 'n'
                    i, j = right(i,j)
                i, j = i, j-1
                if matrix[i+1][j] == 'n':
                    break
                else:
                    i, j = i+1, j
                #down
                while i < m and matrix[i][j] != 'n':
                    ans.append(matrix[i][j])
                    matrix[i][j] = 'n'
                    i, j = down(i,j)
                i,j = i-1, j
                if matrix[i][j-1]=='n':
                    break
                else:
                    i,j = i, j-1
                #left
                while j >= 0 and matrix[i][j] != 'n':
                    ans.append(matrix[i][j])
                    matrix[i][j] = 'n'
                    i, j = left(i,j)
                i, j = i, j+1
                if matrix[i-1][j] == 'n':
                    break
                else:
                    i,j = i-1, j
                #up 
                while i >= 0 and matrix[i][j] != 'n':
                    ans.append(matrix[i][j])
                    matrix[i][j] = 'n'
                    i, j = up(i,j)
                i, j = i+1, j
                if matrix[i][j+1] == 'n':
                    break
                else:
                    i,j = i,j+1
            return ans

 # sol 2.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, result = len(matrix), len(matrix[0]), []
        num_spirals = min(m//2, n//2) # the number of times we spiral (right, down, left, up) through the matrix
        
		# if the matrix is a single row or column, we simply return the elements in order
        if not(m//2 and n//2):
            for i,j in product(range(m), range(n)):
                result.append(matrix[i][j])
            return result
        
		# otherwise, we traverse through the matrix num_spirals times in order
        for i in range(num_spirals):
            for j in range(i,n-i): # traverse right on the top side
                result.append(matrix[i][j])
            for j in range(i+1,m-i-1): # traverse down on the right side
                result.append(matrix[j][n-i-1])
            for j in range(n-i-1,i-1,-1): # traverse left on the bottom side
                result.append(matrix[m-i-1][j])
            for j in range(m-i-2,i,-1): # traverse up on the left side
                result.append(matrix[j][i])
        
		# if the matrix isn't an nxn square, we still need to add elements from the middle
        for i in range(num_spirals, m-num_spirals):
            for j in range(num_spirals, n-num_spirals):
                result.append(matrix[i][j])
                
        return result
