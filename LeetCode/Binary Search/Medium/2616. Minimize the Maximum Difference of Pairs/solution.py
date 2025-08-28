class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N = len(nums)
        nums.sort()

        def count_pairs(limit: int) -> int:
            i = 0
            count = 0
            while i<N-1:
                if nums[i+1]-nums[i]<=limit:
                    count+=1
                    if count == p:
                        return count
                    i+=2
                else:
                    i+=1
            return count

        l, r = 0, nums[-1]-nums[0]
        
        while l<r:
            mid = l + (r-l)//2
            if count_pairs(mid)>=p:
                r = mid
            else:
                l = mid + 1
        return l




        """
        Question:
        nums - List[int]
        p - int
        return min(max(difference among all p pairs))

        Solution:
        Sort the values.
        Use binary search on the answers to find the minimum max difference
        """