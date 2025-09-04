class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stck = []

        for i in nums2:
            while stck and stck[-1]<i:
                nge[stck.pop()] = i
            stck.append(i)

        for i in stck:
            nge[i] = -1

        return [nge[i] for i in nums1]

        """
        Question:
        nums1: List[int] - list of numbers that is subset of nums2
        nums2: List[int] - list of numbers
        return: List[int] = of len nums1 which give index of next greater element in nums2

        Solution:
        We can do a double loop O(n^2)
        But for O(n) we can use a monotonically decreasing stack
        """