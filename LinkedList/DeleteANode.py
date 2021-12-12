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
    def deleteNode(self,key):
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
    

if __name__ == '__main__':
    llist = linkedList()
    
    llist.pushNode(1)
    llist.pushNode(2)
    llist.pushNode(3)
    llist.pushNode(4)
    llist.pushNode(5)
    llist.pushNode(6)
    
    llist.printList()
    
    print("\nllist after deletion, say, 4 and 6\n")
    
    llist.deleteNode(4)
    llist.deleteNode(6)
    llist.printList()
    
    