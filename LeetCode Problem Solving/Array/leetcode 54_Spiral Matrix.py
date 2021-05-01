# Given an m x n matrix, return all elements of the matrix in spiral order.

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
