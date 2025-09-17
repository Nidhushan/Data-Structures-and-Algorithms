# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = x + y + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        
        # dummy = ListNode()
        # head = dummy
        # carry = False
        
        # while l1 or l2:

        #     if l1 and l2:
        #         listSum = l1.val+l2.val
        #         l1, l2 = l1.next, l2.next
        #     elif l1:
        #         listSum = l1.val
        #         l1 = l1.next
        #     elif l2:
        #         listSum = l2.val
        #         l2 = l2.next
            
        #     if carry:
        #         listSum+=1
        #         carry = False

        #     if listSum>=10:
        #         listSum%=10
        #         carry = True

            
            
        #     head.next = ListNode(listSum, None)
        #     head = head.next
        
        # if carry:
        #     head.next = ListNode(1, None)

        # return dummy.next