class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0   
        for i in range(32):
            # Shift result left by 1 to make space for the next bit
            res = res<<1
            # Copy the least significant bit (LSB) of n into res
            res = res | n&1
            # Shift n right by 1 to process the next bit in the next iteration
            n = n>>1
        return res