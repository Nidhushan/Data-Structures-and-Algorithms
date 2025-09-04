class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i]>1:
                return True
        return False
        

        # return len(set(nums)) < len(nums)

        """
        Question:
        nums: List[int] - numbers
        return: bool - does nums contain duplicate

        Solution:
        easy way - find len of set and len of nums
        Freq:
        use a hashmap? if freq>1 return false
        """