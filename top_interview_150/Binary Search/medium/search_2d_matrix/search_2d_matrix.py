class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        pivot = m//2
        start = 0
        end = m

        i = None
        while i is None:
            if matrix[pivot][0] == target:
                return True
            elif pivot == 0 and matrix[pivot][0] > target:
                return False
            elif pivot == m-1 and matrix[pivot][0] < target:
                i = pivot
            elif matrix[pivot][0] < target < matrix[pivot+1][0]:
                i = pivot
            elif matrix[pivot-1][0] < target < matrix[pivot][0]:
                i = pivot - 1

            elif matrix[pivot][0] > target:
                end = pivot
                pivot = (pivot - start) // 2
            elif matrix[pivot][0] < target:
                start = pivot
                pivot = ((end - pivot) // 2) + pivot

        n = len(matrix[i])
        pivot = n//2
        start = 0
        end = n
        while True:
            if matrix[i][pivot] == target:
                return True
            elif pivot == 0 and matrix[i][pivot] > target:
                return False
            elif pivot == n-1 and matrix[i][pivot] < target:
                return False
            elif matrix[i][pivot] < target < matrix[i][pivot+1]:
                return False
            elif matrix[i][pivot-1] < target < matrix[i][pivot]:
                return False

            elif matrix[i][pivot] > target:
                end = pivot
                pivot = (pivot - start) // 2
            elif matrix[i][pivot] < target:
                start = pivot
                pivot = ((end - pivot) // 2) + pivot