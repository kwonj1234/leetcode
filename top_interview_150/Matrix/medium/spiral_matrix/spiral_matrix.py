class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix[0]) == 0:
            return []

        i = 0
        j = 0
        ans = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        curr_direc = (0,1)

        while matrix[i][j] is not None:
            ans.append(matrix[i][j])
            matrix[i][j] = None
            print(i, j)
            if 0 <= i + curr_direc[0] < len(matrix) \
            and 0 <= j + curr_direc[1] < len(matrix[0]) \
            and matrix[i+curr_direc[0]][j+curr_direc[1]] is not None:
                i += curr_direc[0]
                j += curr_direc[1]

            else:
                for direc in directions:
                    if 0 <= i + direc[0] < len(matrix) \
                    and 0 <= j + direc[1] < len(matrix[0]) \
                    and matrix[i+direc[0]][j+direc[1]] is not None:
                        print(direc)
                        curr_direc = direc
                        i += curr_direc[0]
                        j += curr_direc[1]
                        break
        
        return ans