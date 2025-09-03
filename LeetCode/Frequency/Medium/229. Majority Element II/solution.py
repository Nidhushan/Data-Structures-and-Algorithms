class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # freq = Counter(nums)
        # N = len(nums)
        # return [num for num in freq if freq[num]>N//3]

        if not nums:
            return []

        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for c in (candidate1, candidate2):
            if nums.count(c) > len(nums) // 3:
                result.append(c)

        return result

        """
        Question:
        nums: List[int] - numbers
        return: List[int] - numbers that occur more than n//3 times

        Solution:
        Freq hashmap, return any that have more freq than n//3

        Boyer-Moore Voting Algorithm
        you’re guaranteed that at most two elements can appear more than ⌊n/3⌋ times. So we can track only two candidates.
        """