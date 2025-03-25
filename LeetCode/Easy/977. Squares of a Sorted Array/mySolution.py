class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(nums) - 1

        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])

            if left > right:
                answer.appendleft(left * left)
                l += 1

            else:
                answer.appendleft(right * right)
                r -= 1

        return list(answer)

        # Easy straightforward solution
        
        # res = []
        # for i in nums:
        #     res.append(i**2)
        
        # res = sorted(res)
        # return res