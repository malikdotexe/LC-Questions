class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        srow = 0
        ecol = len(matrix[0])-1

        while srow<=len(matrix)-1 and ecol>=0:
            a = matrix[srow][ecol]
            if target<a:
                ecol-=1
            elif target>a:
                srow+=1
            else:
                return True
        return False
