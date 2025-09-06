# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

        """
        Question:
        head: ListNode - first node in Sorted List
        return ListNode - first node in the list after removing duplicates

        Solution:
        LinkedList - if next val is same as cur val, remove the next element
        """