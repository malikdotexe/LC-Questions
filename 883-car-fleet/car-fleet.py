class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [[position[i],speed[i]] for i in range(len(position))]
        data.sort(key = lambda x:x[0])
        time = [0]*len(position)
        for i in range(len(data)):
            time [i] = (target-data[i][0])/data[i][1]
        stack = []
        
        #Track number of values which dont have any greater values in front of them
        ans = 0
        
        #for loop is identical to next greater solution
        for i in range(len(time)-1,-1,-1):
            t = time[i]
            while stack and t>stack[-1]:
                    stack.pop()
            #No greater value exists
            if not stack:
                ans+=1
                stack.append(t)
            if stack:
                stack.append(t)
                 

            

        return ans