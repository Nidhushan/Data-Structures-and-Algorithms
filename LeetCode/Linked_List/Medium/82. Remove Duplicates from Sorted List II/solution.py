# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(0, head)
        # prev = dummy
        # cur = head

        # while cur and cur.next:
        #     if cur.val == cur.next.val:
        #         while cur.next and cur.val == cur.next.val:
        #             cur.next = cur.next.next
        #         prev.next = cur.next
        #         cur = cur.next
        #         continue

        #     prev = cur
        #     cur = cur.next
            
        # return dummy.next

        # Cleaner version:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            # skip all nodes with the same value
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            # if prev.next != cur, we saw duplicates → unlink them
            if prev.next != cur:
                prev.next = cur.next
            else:
                prev = prev.next  # no duplicates, move prev forward

            cur = cur.next

        return dummy.next

        """
        Question:
        head: ListNode - head of a SLL
        return: ListNode - head of the same SLL after removing duplicates along with their original

        Solution:
        use a while loop to recurringly remove duplicates, once done, remove the original
        """