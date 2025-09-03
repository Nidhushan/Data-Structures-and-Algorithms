class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        return int((sum(set(nums))*3 - sum(nums))/2)
        
        # freq = Counter(nums)

        # for i in nums:
        #     if freq[i] == 1:
        #         return i
        


        """
        Question:
        nums: List[int]: array with every element appearing 3 times except 1 which appears once
        return: int: element that appears once

        Solution:
        Create a hashmap and store frequencies
        loop to get the one with freq = 1

        #2 using sums of the elements

        #3 Using bit manipulation

        """