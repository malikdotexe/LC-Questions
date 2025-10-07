class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows-1
        targetrow = False
        while l<=r:
            midr = l+(r-l)//2
            if matrix[midr][0]<=target and matrix[midr][cols-1]>=target:
                targetrow = matrix[midr]
                break
            elif matrix[midr][0]>target:
                r = midr-1
            elif matrix[midr][cols-1]<target:
                l = midr+1
        l = 0
        r = cols-1
        if targetrow == False:
            return False
        ans = False
        while l<=r:
            mid = l +(r-l)//2
            if targetrow[mid]<target:
                l = mid+1
            elif targetrow[mid]>target:
                r = mid-1
            else:
                ans = True
                break
        return ans