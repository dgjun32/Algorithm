# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# solution 1.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i+1, n):
                a, b = matrix[i][j], matrix[j][i]
                matrix[i][j], matrix[j][i] = b, a
        # flipping matrix horizontally
        for k in range(n):
            matrix[k] = matrix[k][::-1]
        return matrix

# solution 2. More efficient and simpler approach
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        for row in zip(*matrix):
            matrix[i] = list(row)[::-1]
            i += 1
        return matrix
