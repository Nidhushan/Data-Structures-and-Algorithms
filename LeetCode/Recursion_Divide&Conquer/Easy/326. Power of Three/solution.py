class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Recursive:
        # if n==1:
        #     return True
        
        # if n<=0 or n%3!=0:
        #     return False

        # return self.isPowerOfThree(n//3)

        # Without recursion or loop:
        # return n>0 and 1162261467%n==0

        # With looping:
        if n<=0:
            return False
        while n%3==0:
            n=n//3
        return n==1

        """
        Question:
        n: int - number
        return: bool - if n is a power of three

        Solution:
        recursion by dividing n each time
        without loop possible?
        1 =  0000001
        3 =  0000011
        9 =  0000101
        27 = 0011011
        81 = 1010001
        """