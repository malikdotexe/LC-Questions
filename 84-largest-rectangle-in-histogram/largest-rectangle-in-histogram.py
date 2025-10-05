class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #previous smaller array
        s1=[]
        ps=heights.copy()
        for i,h in enumerate(heights):   
            while s1 and s1[-1][0]>=h:
                s1.pop()
            if not s1:
                ps[i]=-1
                s1.append([h,i])
            if  s1[-1][0]<h:
                ps[i]=s1[-1][1]
                s1.append([h,i])
        #next smaller array
        ns= heights.copy()
        s2=[]
        for i in range(len(heights)-1,-1,-1):

            while s2 and s2[-1][0]>=heights[i]:
                s2.pop()
            if not s2:
                ns[i]=len(heights)
                s2.append([heights[i],i])
            if s2[-1][0]<heights[i]:
                ns[i]=s2[-1][1]
                s2.append([heights[i],i]) 
        width = [ns[i] - ps[i]-1 for i in range(len(ns))]
        #final calculation
        maxarea= 0
        for i,num in enumerate(heights):
                currarea = num * width[i]
                maxarea = max(currarea,maxarea)
        return maxarea