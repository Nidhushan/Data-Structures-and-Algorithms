# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive:
        if not head or not head.next:
            return head
        
        newHead =  self.reverseList(head.next)
        
        head.next.next = head
        head.next = None

        return newHead

        # Iterative
        # current = head
        # prev = None

        # while (current!=None):
        #     next_pointer = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_pointer
        
        # head = prev
        # return head

        """
        Question:
        head: ListNode - head of a SLL
        return: ListNode - head of the SLL after reversing it

        Solution:
        iterative:
        loop through and reverse each and return the new head

        Recursive:

        """

