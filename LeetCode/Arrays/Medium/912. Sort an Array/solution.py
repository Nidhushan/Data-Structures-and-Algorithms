class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(l, r):
            if l>=r: return

            p = random.randint(l, r)
            nums[l], nums[p] = nums[p], nums[l]
            pivot = nums[l]

            lt, i, gt = l, l+1, r

            while i<=gt:
                if nums[i]<pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt+=1; i+=1
                elif nums[i]>pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt-=1
                else:
                    i+=1
            
            quickSort(l, lt-1)
            quickSort(gt+1, r)
        
        quickSort(0, len(nums)-1)
        return nums
        
        # n = len(nums)
        # temp = [0]*n

        # def mergeSort(l, r):
        #     if (r-l)<=1: return
        #     m = (r+l)//2
        #     mergeSort(l,m)
        #     mergeSort(m,r)
        #     i, j, k = l, m, l

        #     while i<m and j<r:
        #         if nums[i]<=nums[j]:
        #             temp[k] = nums[i]; i+=1
        #         else:
        #             temp[k] = nums[j]; j+=1
        #         k+=1
        #     while i<m: temp[k] = nums[i]; i+=1; k+=1
        #     while j<r: temp[k] = nums[j]; j+=1; k+=1

        #     nums[l:r] = temp[l:r]
        
        # mergeSort(0, n)
        # return nums

        
        # def mergeSort(arr: List[int]) -> List[int]:
        #     if len(arr)<=1:
        #         return arr
        #     mid = len(arr)//2
        #     left = mergeSort(arr[:mid])
        #     right = mergeSort(arr[mid:])

        #     return merge(left, right)
        # def merge(a: List[int], b: List[int]) -> List[int]:
        #     i = j = 0
        #     out = []

        #     while i<len(a) and j<len(b):
        #         if a[i]<=b[j]:
        #             out.append(a[i])
        #             i+=1
        #         else:
        #             out.append(b[j])
        #             j+=1
            
        #     out.extend(a[i:]); out.extend(b[j:])
        #     return out
        
        # return mergeSort(nums)
            
        """
        Question:
        implement in place sorts. Since its O(nlogn), either merge sort or insertion sort.

        Solution:
        Merge sort:
        keep splitting the array and apply merge sort on the left and right halves

        Quick Sort
        make a pivot
        make 3 partitions, <pivot, =pivot, >pivot
        recurse on the <pivot and >pivot
        """