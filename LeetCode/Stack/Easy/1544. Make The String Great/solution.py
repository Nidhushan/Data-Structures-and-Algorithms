class Solution:
    def makeGood(self, s: str) -> str:
        stck = []

        # Better Runtime 
        for i in s:
            if stck and abs(ord(stck[-1]) - ord(i)) == 32:
                stck.pop()
            else:
                stck.append(i)
                
        # Better Memory
        # for i in s:
        #     if not stck or abs(ord(stck[-1]) - ord(i)) != 32:
        #         stck.append(i)
        #     else:
        #         stck.pop()


        return "".join(stck)


        """
        Question:
        s: string
        return: string: make s good and return it

        Solution:
        put it in a stack and pop characters that dont make s good.
        """