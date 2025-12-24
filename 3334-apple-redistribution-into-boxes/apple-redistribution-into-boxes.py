class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse =True)
        cap = 0
        i = 0
        while cap<total:
            cap += capacity[i]
            i+=1
            print(f"cap {cap} and total {total}")
        return i