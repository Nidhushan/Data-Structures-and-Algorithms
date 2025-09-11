# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val<list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # dummy = curr = ListNode()

        # while list1 and list2:
        #     if list1.val<list2.val:
        #         curr.next = list1
        #         list1, curr = list1.next, list1
        #     else:
        #         curr.next = list2
        #         list2, curr = list2.next, list2
        
        # if list1 or list2:
        #     curr.next = list1 if list1 else list2
        
        # return dummy.next

        """
        Question:
        list1: ListNode - head of list 1 a sorted SLL
        list2: ListNode = head of list 2 a sorted SLL
        return: ListNode - head of merged list
        
        Solution:
        recursively merge the two
        """
