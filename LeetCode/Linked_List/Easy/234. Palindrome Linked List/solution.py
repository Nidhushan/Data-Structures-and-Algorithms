# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # More Efficient Solution:
        if not head or not head.next:
            return True

        # reverse first half while moving slow/fast
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev   # reverse link
            prev = slow
            slow = nxt

        # if odd length, skip middle node
        if fast:  # fast not None => odd length
            slow = slow.next

        # compare reversed first half (prev) with second half (slow)
        p1, p2 = prev, slow
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
        
        
        
        # slow, fast = head, head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # prev = None

        # while slow:
        #     slow.next, prev, slow  = prev, slow, slow.next

        # slow = head

        # while prev:
        #     if prev.val !=  slow.val:
        #         return False
        #     prev = prev.next
        #     slow = slow.next
        # return True

        """
        Question:
        head: ListNode - head of a SLL
        return: bool - if the SLL is a palindrome

        Solution:
        find the middle
        reverse from middle
        check from middle and start, if not equal return false

        """
        