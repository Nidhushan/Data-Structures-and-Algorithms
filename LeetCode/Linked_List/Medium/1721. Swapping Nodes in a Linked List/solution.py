# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy = ListNode(0, head)
        # cur = head
        # count = 0
        # while cur:
        #     cur = cur.next
        #     count+=1
        # cur = head
        # for i in range(1, count+1):
        #     if i==k:
        #         startNode = cur
        #     if i==count-k+1:
        #         endNode = cur
        #     cur = cur.next
        # temp = startNode.val
        # startNode.val = endNode.val
        # endNode.val = temp

        # return head

        # More efficient way
        # kth from start
        first = head
        for _ in range(k - 1):
            first = first.next

        # kth from end: advance fast k-1, then move slow & fast
        slow = head
        fast = head
        for _ in range(k - 1):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        second = slow

        # swap values
        first.val, second.val = second.val, first.val
        return head

        """
        Question:
        head: ListNode - head of a SLL
        k: int - position of node to be swapped(from start and end)
        return: ListNode - head of the SLL after swapping

        Solution:
        loop through and find the length
        swap the values in another loop
        """