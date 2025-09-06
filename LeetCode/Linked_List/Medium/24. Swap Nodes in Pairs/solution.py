# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head
        # dummy = head.next
        # prev, cur, nxt = head, head, head.next
        # cur.next = nxt.next
        # nxt.next = cur
        # if cur.next:
        #     cur = cur.next
        #     nxt = cur.next
        # else:
        #     return dummy

        # while cur and cur.next:
        #     cur.next = nxt.next
        #     nxt.next = cur
        #     prev.next = nxt
        #     prev = cur
        #     cur = cur.next
        #     if cur:
        #         nxt = cur.next
        #     else:
        #         return dummy

        # return dummy

        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            nxt = cur.next

            cur.next = nxt.next
            nxt.next = cur
            prev.next = nxt

            prev = cur
            cur = cur.next

        return dummy.next


        """
        Question:
        head: ListNode - head of a singly linked list
        return: ListNode - head of the singly linked list after swaping every two adjacent nodes

        Solution:
        having prev, cur and next, swap the nodes.

        [1,2,3,4,5,6]
        [2,1,3,4,5,6]
        [2,1,4,3,5,6]
        [2,1,4,3,6,5]

        """