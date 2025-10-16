from collections import defaultdict
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        #Frequency map for Remainder
        remfreq =defaultdict(int)
        #Set for storing all the values we could attain by doing ops
        ans = set()

        for num in nums:
            rem = num%value
            #If we are seeing the remainder for the first time we would simply add that to our set
            if remfreq[rem]==0:
                remfreq[rem]+=1
                ans.add(rem)
            #else there is no benefit in adding the same remainder rather we would use it go to a higher number by adding our value to it. Eg if value = 3 and we have "0" as a remainder already in set we would add 0+3 to the set and later if we found 0 remainder again we would add 0+3+3 to the set
            else:
                count = remfreq[rem]
                ans.add(rem+(value*(count)))
                remfreq[num%value]+=1
        #Simple loop to find where the sequence breaks
        maximum = max(ans)
        for i in range(0,maximum):
            if i not in ans:
                return i
        #Edge case where we have complete sequence
        return maximum+1