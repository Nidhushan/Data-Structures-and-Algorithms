# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

        """
        Question:
        head: ListNode - the start of a singly linked list
        return: ListNode - the middle of the singly linked list

        Solution:
        use Floyd's hare and tortoise method to solve
        """