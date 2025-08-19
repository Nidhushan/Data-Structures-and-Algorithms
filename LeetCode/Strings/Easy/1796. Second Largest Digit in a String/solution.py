class Solution:
    def secondHighest(self, s: str) -> int:
        l = False
        for i in range(9, -1, -1):
            if str(i) in s:
                if l:
                    return i
                l = True
        
        return -1


        
        # s = set([int(i) for i in s if i.isdigit()])

        # if len(s)<2:
        #     return -1

        # first = second = float('-inf')
        # for i in s:
        #     if i>first:
        #         second = first
        #         first = i
        #     elif first>i>second:
        #         second = i
        
        # return second

            
        """
        Question:
        s - String
        find second largest digit in string

        Solution:
        find all unique digits
        return second largest in it.
        """