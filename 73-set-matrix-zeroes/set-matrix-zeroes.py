class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        firstrow = 1
        for m in range(rows):
            for n in range(cols):
                if matrix[m][n]==0:
                    matrix[0][n]=0
                    if m>0:
                        matrix[m][0]=0 
                    else:
                        firstrow=0
        for m in range(1,rows):
            for n in range(1,cols):
                if matrix[m][0]==0 or matrix[0][n]==0:
                    matrix[m][n]=0
        if matrix[0][0]==0:
            for m in range(rows):
                matrix[m][0]=0
        if firstrow == 0:
            for n in range(cols):
                matrix[0][n]=0

