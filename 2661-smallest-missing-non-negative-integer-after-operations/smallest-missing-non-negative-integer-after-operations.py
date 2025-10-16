from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        #Frequency map for Remainder
        remfreq = Counter(num % value for num in nums)
        i = 0
        while True:
            r = i % value
            #If we run out of that remainder
            if remfreq[r] == 0:
                return i
            #Decrease count of the remainder we have used
            remfreq[r] -= 1
            #i starts from 0 and goes till its remainder with value is not found
            i += 1
