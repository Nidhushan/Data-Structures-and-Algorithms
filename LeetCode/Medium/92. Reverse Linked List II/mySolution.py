# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(-501, head)

        left_prev, current_node = dummy_head, head

        for i in range(left-1):
            left_prev, current_node = current_node, current_node.next

        prev = None

        for i in range(right-left+1):
            next_pointer = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_pointer
        
        left_prev.next.next = current_node
        left_prev.next = prev

        return dummy_head.next

