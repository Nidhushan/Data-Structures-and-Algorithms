class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left  # or right — they are equal here
        
        # n = len(arr)
        # left = 1
        # right = len(arr) - 2

        # while left <= right:
        #     mid = (left + right) // 2  # or: left + (right - left) // 2
        #     if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
        #         return mid
        #     elif arr[mid+1]>arr[mid] and arr[mid]>arr[mid-1]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return -1  # target not found

