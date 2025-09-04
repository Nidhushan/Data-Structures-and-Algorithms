class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq = {}
        # N = len(nums)

        # for i in nums:
        #     freq[i] = freq.get(i, 0) + 1
        #     if freq[i]>N//2:
        #         return i

        
        # Boyer–Moore Majority Vote
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

        """
        Question:
        nums: List[int] - numbers
        return: int - numner that appears more than n/2 times

        Solution:
        loop through and when a number hits freq>n/2 return it
        """