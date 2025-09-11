class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Recursion:

        # if n==1:
        #     return True
        
        # if n<=0 or n%2!=0:
        #     return False
        
        # return self.isPowerOfTwo(n//2)

        # No loop or recursion:
        return n>0 and (n&(n-1)==0)

        """
        Question:
        n: int - a number
        return: bool - if n is a power of 2

        Solution:
        recursion and divide each time
        """