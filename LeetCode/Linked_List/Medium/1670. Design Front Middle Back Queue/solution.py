class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class FrontMiddleBackQueue:

    # More efficient solution using 2 deques:
    def __init__(self):
        self.L = deque()  # left half
        self.R = deque()  # right half

    def _rebalance(self):
        # keep len(L) == len(R) or len(L) == len(R)+1
        while len(self.L) > len(self.R) + 1:
            self.R.appendleft(self.L.pop())
        while len(self.L) < len(self.R):
            self.L.append(self.R.popleft())

    def pushFront(self, val: int) -> None:
        self.L.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.L) > len(self.R):
            self.R.appendleft(self.L.pop())
        self.L.append(val)
        self._rebalance()

    def pushBack(self, val: int) -> None:
        self.R.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.L and not self.R:
            return -1
        val = self.L.popleft() if self.L else self.R.popleft()
        self._rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.L and not self.R:
            return -1
        val = self.L.pop()
        self._rebalance()
        return val

    def popBack(self) -> int:
        if not self.L and not self.R:
            return -1
        val = self.R.pop() if self.R else self.L.pop()
        self._rebalance()
        return val

    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.size = 0

    # def pushFront(self, val: int) -> None:
    #     if not self.head:
    #         self.head = Node(val)
    #         self.tail = self.head
    #         self.size+=1
    #         return
        
    #     temp = Node(val, self.head)
    #     self.head.prev = temp
    #     self.head = temp
    #     self.size+=1

    # def pushMiddle(self, val: int) -> None:
    #     if not self.head:
    #         self.head = Node(val)
    #         self.tail = self.head
    #         self.size+=1
    #         return
    #     if not self.head.next:
    #         newNode = Node(val, self.head)
    #         self.head.prev = newNode
    #         self.head = newNode
    #         self.size+=1
    #         return
    #     else:
    #         dummy = Node(0, self.head)
    #         slow, fast = dummy, self.head
    #         while fast and fast.next:
    #             slow = slow.next
    #             fast = fast.next.next
    #         newNode = Node(val, slow.next, slow)
    #         slow.next.prev = newNode
    #         slow.next = newNode
    #         self.size+=1
            
    # def pushBack(self, val: int) -> None:
    #     if not self.head:
    #         self.head = Node(val)
    #         self.tail = self.head
    #         self.size+=1
    #         return
    #     newNode = Node(val, None, self.tail)
    #     self.tail.next = newNode
    #     self.tail = newNode
    #     self.size+=1


    # def popFront(self) -> int:
    #     if not self.head:
    #         return -1
    #     val = self.head.val
    #     self.head = self.head.next
    #     if not self.head:
    #         self.tail = None
    #     else:
    #         self.head.prev = None
    #     self.size-=1
    #     return val

    # def popMiddle(self) -> int:
    #     if not self.head:
    #         return -1

    #     n = self.size
    #     idx = (n - 1) // 2   # frontmost middle (0-based)

    #     # Find the middle node by walking from the nearer end
    #     if idx <= (n - 1 - idx):
    #         # walk forward from head
    #         cur = self.head
    #         for _ in range(idx):
    #             cur = cur.next
    #     else:
    #         # walk backward from tail
    #         cur = self.tail
    #         steps = n - 1 - idx
    #         for _ in range(steps):
    #             cur = cur.prev

    #     val = cur.val

    #     # unlink cur safely (handle head/tail cases)
    #     if cur.prev:
    #         cur.prev.next = cur.next
    #     else:
    #         self.head = cur.next

    #     if cur.next:
    #         cur.next.prev = cur.prev
    #     else:
    #         self.tail = cur.prev

    #     self.size -= 1
    #     return val


    # def popBack(self) -> int:
    #     if not self.head:
    #         return -1
        
    #     val = self.tail.val
    #     if self.head == self.tail:
    #         self.head = self.tail = None
    #     else:
    #         self.tail = self.tail.prev
    #         self.tail.next = None
    #     self.size-=1
    #     return val
        
        """
        Question:
        design front middle back queue

        Solution:
        do it?
        """

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()