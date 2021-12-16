class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def search(self, x):
        current = self.head

        while current != None:
            if current.data == x:
                return True

            current = current.next

        return False

    def searchRec(self, li, key):
        if(not li):
            return False

        if(li.data == key):
            return True

        return self.search(li.next, key)


if __name__ == '__main__':
    llist = LinkedList()

    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.push(50)
    llist.push(60)

    if llist.search(60):
        print("Yes")
    else:
        print("No")

    if llist.searchRec(50):
        print("Recursive Yes")
    else:
        print("Recursive No")
