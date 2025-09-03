class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = 0

        for i in nums:
            sum ^= i

        return sum



        """
        Question: 
        nums --> List
        Has one unique number, find it.

         Constraints:
         Linear runtime, use only constant extra space.

        di = {}
        for loop:
            store frequencies of each element
        return element with freq 1

        #2 XOR
        using XOR would result in 0 for any two of the same numbers
        So whichever no is only available once would remain
        """