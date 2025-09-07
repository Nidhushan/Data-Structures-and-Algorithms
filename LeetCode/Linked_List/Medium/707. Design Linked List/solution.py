class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index>=self.size or index<0:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        dummy = Node(val, self.head)
        self.head = dummy
        self.size+=1

    def addAtTail(self, val: int) -> None:
        if not self.head:                  # empty list
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # Normalize per LC 707 rules
        if index < 0:
            index = 0
        if index > self.size:
            return  # invalid; do nothing

        dummy = Node(0, self.head)
        prev = dummy
        # move prev to node just before insertion point
        for _ in range(index):
            prev = prev.next  # safe because index ≤ size and dummy leads to head

        prev.next = Node(val, prev.next)
        self.head = dummy.next
        self.size += 1
        


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        dummy = Node(0, self.head)
        prev = dummy
        for _ in range(index):
            prev = prev.next

        # delete node
        prev.next = prev.next.next

        # update head and size
        self.head = dummy.next
        self.size -= 1
        

        """
        Question:
        design your own linked list with its own functionalities
        Solution:
        Do it?
        """


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)