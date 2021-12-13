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
            
    def pushNode(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    
    #can be done recursively. figure it out for yourself    
    def deleteNodeWithKey(self,key):
        temp = self.head
        
        if(temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
        if (temp == None):
            return
        
        prev.next = temp.next
        
        temp=None
    
    def deleteNodeWithPosi(self,pos):
        temp = self.head

        if(temp is not None):
            if pos==1:
                self.head = temp.next
                temp = None
                return
        
        for i in range(pos-1):
            prev = temp
            temp = temp.next

        if(temp == None):
            return
        prev.next = temp.next
        temp=None
        
    

if __name__ == '__main__':
    llist = linkedList()
    
    llist.pushNode(1)
    llist.pushNode(2)
    llist.pushNode(3)
    llist.pushNode(4)
    llist.pushNode(5)
    llist.pushNode(6)
    llist.pushNode(7)
    llist.pushNode(8)
    llist.pushNode(9)
    llist.pushNode(0)
    llist.pushNode(10)
    
    llist.printList()
    
    print("\nNow lets try deletion\n")
    
    llist.deleteNodeWithKey(4)
    llist.deleteNodeWithKey(6)
    print("\nKey deletion done at 4,6\n")
    llist.printList()

    llist.deleteNodeWithPosi(3)
    llist.deleteNodeWithPosi(4)
    print("\nposition deletion done at 3,4\n")
    llist.printList()
    
    