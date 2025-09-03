class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # freq = Counter(nums)
        # res = []
        # cnt = 0
        # for i in nums:
        #     if freq[i] == 1:
        #         cnt+=1
        #         res.append(i)
        #         if cnt == 2:
        #             return res
        # return res

        freq = Counter(nums)
        return [num for num in freq if freq[num] == 1]

        # seen = set()

        # for i in nums:
        #     if i in seen:
        #         seen.remove(i)
        #     else:
        #         seen.add(i)
        # return list(seen)


        """
        Question:
        nums: List[int] - has two elements appear once and all others appear twice exactly
        return: List[int] - the two elements appearing once

        Solution:
        #1 Create a hashmap of frequencies
        return the ones with frequency 1
        #2 Use sets, to add and remove, so the ones with 1 freq only add
        """