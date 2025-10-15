class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        arr = [int(digit) for digit in str(abs(x))]
        l = 0
        r = len(arr)-1
        while l<r:
            if arr[l]!=arr[r]:
                return False
            l+=1
            r-=1
        return True

