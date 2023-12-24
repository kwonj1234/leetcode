# Bad Solution
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         zero_rows = []
#         zero_cols = []

#         m = len(matrix)
#         n = len(matrix[0])

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     if i not in zero_rows:
#                         zero_rows.append(i)
#                     if j not in zero_cols:
#                         zero_cols.append(j)
        
#         for i in range(m):
#             for j in range(n):
#                 if i in zero_rows:
#                     matrix[i][j] = 0
#                 elif j in zero_cols:
#                     matrix[i][j] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for a in range(m):
                        if matrix[a][j] != 0:
                            matrix[a][j] = None
                    for b in range(n):
                        if matrix[i][b] != 0:
                            matrix[i][b] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0