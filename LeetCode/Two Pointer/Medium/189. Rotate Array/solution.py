class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        N = len(nums)
        k %= N
        print(N, k)

        def reverse(start, end):
            print("entered")
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
            
        reverse(0, N-1)
        reverse(0, k-1)
        reverse(k, N-1)

        """
        Question:
        nums - List[int]
        k - int
        Rotate the list by k times

        Solution:
        reverse the whole list, then reverse back in two parts:
        once upto k, then from k to len(nums)
        """