# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle point
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None

        while slow!=None:
            next_pointer = slow.next
            slow.next = prev
            prev = slow
            slow = next_pointer
        
        # Check if second half equal to the first half 
        left, right = head, prev

        while right!=None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
        