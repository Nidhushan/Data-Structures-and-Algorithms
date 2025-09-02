class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        st = []
        for d in num:
            while k and st and st[-1] > d:
                st.pop()
                k -= 1
            st.append(d)

        if k:
            st = st[:-k]

        res = "".join(st).lstrip("0")
        return res or "0"


        # stck = []
        
        # for digit in num:

        #     while k>0 and stck and stck[-1]>digit:
        #         stck.pop()
        #         k-=1
        #     stck.append(digit)
        
        # while k>0:
        #     stck.pop()
        #     k-=1
        
        # result = "".join(stck).lstrip("0")
        # return result if result else "0"

        """
        Question:
        num: str: non negative integer number representation
        k: int: no. of numbers you can remove
        return: str: string representation of a number after removing k elements

        Solution:
        Use a stack and pop the number k times if stck[-1]>digit
        """ 