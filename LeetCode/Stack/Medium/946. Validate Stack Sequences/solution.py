class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stck = []
        j = 0
        for i in pushed:
            stck.append(i)
            while stck and j<len(pushed) and stck[-1]==popped[j]:
                stck.pop()
                j+=1
        return not stck
            


        """
        Question:
        pushed: List[int]: list of numbers pushed in
        popped: List[int]: List of numbers popped out(in sequence)
        return: bool: is it possible to pop it in that sequence

        Solution:
        use a stack to push and pop when the value is met
        """