class Solution:
    def totalMoney(self, n: int) -> int:        
        i=0
        days = 0   
        sum = 0 
        increment = 0
        while days!=n:
            sum +=i+1+increment
            days+=1
            i = (i+1)%7
            #increase increment by 1 if one week completes
            if i==0:
                increment+=1
            
        return sum