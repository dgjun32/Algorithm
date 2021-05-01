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
