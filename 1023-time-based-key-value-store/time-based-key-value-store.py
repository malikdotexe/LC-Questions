from collections import defaultdict
class TimeMap:

    def __init__(self):
        #hashmap
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str :
        
        l = 0
        r = len(self.store[key])-1
        ans = None
        while l<=r:
            mid = l+(r-l)//2
            data = self.store[key][mid]
          
            #if mid time is bigger than timestamp shift to right part while storing the closest value
            if data[1]>timestamp:
                r = mid-1
            #if mid time is smaller than timestamp shift to left part of store
            elif data[1]<timestamp:
                #Update ans value to new found if its bigger than ans
                if not ans:
                    ans = data
                if ans:
                    if data[1]>=ans[1]:
                        ans = data
                l = mid+1
            #exact match
            else:
                return data[0]

        if ans: 
            return ans[0]
        else:
            return ""
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)