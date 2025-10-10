from collections import defaultdict
class TimeMap:

    def __init__(self):
        #hashmap
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str :
        
        l = 0
        values = self.store[key]
        r = len(values)-1
        ans = ""
        while l<=r:
            mid = l+(r-l)//2
            data = values[mid]
            #if mid time is smaller than timestamp shift to left part of store
            
            if data[1]>timestamp:
                r = mid-1
            #if mid time is bigger or equal to timestamp shift to right part while storing the closest value
            else:
                ans = data[0]
                l = mid+1
                
           

        return ans
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)