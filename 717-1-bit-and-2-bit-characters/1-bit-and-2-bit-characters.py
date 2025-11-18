class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1:return True
        if bits[-2]==1:
            #check if 1s are even
            ones = 0
            i=len(bits)-2
            while bits[i]==1:
                ones+=1
                i-=1
            if ones>0 and ones%2==0:
                return True
            else:
                return False
        return True
            
        
            