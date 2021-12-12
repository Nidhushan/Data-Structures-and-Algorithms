class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def insertAtHead(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        
    def insertAfterAnElement(self,prev_node,data):
        if prev_node==None:
            print("given previous node is None")
            return
        
        temp = Node(data)
        
        temp.next = prev_node.next
        prev_node.next = temp
        
    def insertAtEnd(self,data):
        temp = Node(data)
        
        if self.head is None:
            self.head = temp
            return
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = temp

if __name__ == '__main__':
    llist = linkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    
    second.next = third
    
    
    
    llist.insertAtHead(6)
    llist.insertAfterAnElement(second,7)
    llist.insertAtEnd(10)
    llist.printList()
    