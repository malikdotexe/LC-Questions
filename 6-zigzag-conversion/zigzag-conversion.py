class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s = list(s)
        matrix = [[] for n in range(numRows)]

        p= 0 
        while p<len(s):
            #down loop
            for i in range(numRows):
                if p<len(s):
                    matrix[i].append(s[p])
                    p+=1
            #diagonal loop
            for i in range(numRows-2,0,-1):
                if p<len(s):
                    matrix[i].append(s[p])
                    p+=1
        
        res = ""
        for arr in matrix:
            string ="".join(arr)
            res += string
        return res