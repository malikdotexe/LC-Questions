class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #previous smaller array
        s1=[]
        ps=[0]*len(heights)
        for i in range(len(heights)):   
            while s1 and heights[s1[-1]]>=heights[i]:
                s1.pop()
            if not s1:
                ps[i]=-1
                s1.append(i)
            else:
                ps[i] = s1[-1]
                s1.append(i)
        #next smaller array
        ns=[0]*len(heights)
        s2=[]
        for i in range(len(heights)-1,-1,-1):
            while s2 and heights[s2[-1]]>=heights[i]:
                s2.pop()
            if not s2:
                ns[i]=len(heights)
                s2.append(i)
            else:
                ns[i]=s2[-1]
                s2.append(i) 
        width = [ns[i] - ps[i]-1 for i in range(len(ns))]
        #final calculation
        maxarea= 0
        for i,num in enumerate(heights):
                currarea = num * width[i]
                maxarea = max(currarea,maxarea)
        return maxarea