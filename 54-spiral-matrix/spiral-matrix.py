class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        srow = 0 
        erow = r-1
        #erow=3
        scol = 0
        ecol = c-1
        #ecol = 3
        res = []


        #to traverse row=> fix row and iterate column
        while srow <= erow and scol <= ecol:
            #top left to top right loop(row) [0][0] - [0][3]
            for i in range(scol,ecol+1):
                res.append(matrix[srow][i])


            #top right to bottom right loop(col) [1][3]-[3][3]
            for i in range(srow+1,erow+1):
                res.append(matrix[i][ecol])


            if srow<erow:
                #bottom right to bottom left loop(row) [3][2] - [3,0]
                for i in range(ecol-1, scol-1,-1):
                    res.append(matrix[erow][i])

            if scol<ecol:
                #bottom left to top left loop(col) [2,0]-[1,0]
                for i in range(erow-1,srow,-1):
                    res.append(matrix[i][scol])
            srow+=1
            erow-=1
            scol+=1
            ecol-=1
        return res

