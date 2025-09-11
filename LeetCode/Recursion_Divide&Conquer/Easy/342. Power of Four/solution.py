class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Recursion:

        # if n==1:
        #     return True
        # if n>0 and n%4!=0:
        #     return False
        # if n<=0:
        #     return False
        
        # return self.isPowerOfFour(n//4)

        # without loops or recursion
        if n < 0:
            return False
        else:
            return (n & (n - 1) == 0) and (n & 0x55555555 != 0)

        """
        Question:
        n: int - number
        return: bool - if n is a power of four

        Solution:
        recursive check with division by four handling negatives
        """