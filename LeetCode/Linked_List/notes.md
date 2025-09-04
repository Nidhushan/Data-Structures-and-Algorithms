# Linked Lists — Complete Notes (from Basics to Advanced)

> **Core idea:** A linked list stores elements in **nodes**. Each node holds a value and one or more **references** (pointers) to other nodes. Unlike arrays, nodes are not necessarily contiguous in memory. This enables **O(1)** insertion/deletion given a pointer to the location, but **O(n)** positional access.

---

## 0) Quick Complexity Table

| Operation | Singly LL | Doubly LL | With Tail Ptr |
|---|---:|---:|---:|
| Access by index `i` | O(n) | O(n) | O(n) |
| Search by value | O(n) | O(n) | O(n) |
| Insert at head | **O(1)** | **O(1)** | **O(1)** |
| Insert at tail | O(n) | O(n) | **O(1)** |
| Delete at head | **O(1)** | **O(1)** | **O(1)** |
| Delete at tail | O(n) | O(1) if prev known | O(1) if doubly + tail |
| Insert/Delete at known node | **O(1)** | **O(1)** | **O(1)** |

Space: O(n) for `n` nodes.

---

## 1) Node & List Definitions

### Singly Linked List (SLL)
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
- Each node knows only its `next`.
- Minimal memory; many LeetCode problems use this.

### Doubly Linked List (DLL)
```python
class DListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```
- Nodes know `prev` **and** `next`.
- Easier O(1) delete given the node, easy tail ops; slightly larger memory.

### Circular LL
- Tail points back to head. Useful for round-robin / cycles.

### Sentinel (Dummy) Nodes
- **Dummy head/tail** simplify edge cases (insert/delete at head/tail) by making every operation a middle-case operation.

---

## 2) When to Choose Linked Lists vs Arrays

**Pick LL when:** frequent insertion/deletion in the middle or at ends, unknown size, no need for random access.

**Pick array when:** frequent indexed access, better cache locality, simpler memory.

---

## 3) Fundamental Operations (SLL) with Patterns

### 3.1 Insert at Head — O(1)
```python
# Time: O(1), Space: O(1)
def push_front(head: ListNode | None, val: int) -> ListNode:
    node = ListNode(val)
    node.next = head
    return node
```

### 3.2 Insert at Tail — O(n) or O(1) with tail pointer
```python
# Time: O(n) if no tail; Space: O(1)
def push_back(head: ListNode | None, val: int) -> ListNode:
    node = ListNode(val)
    if not head:
        return node
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = node
    return head
```

### 3.3 Delete at Head — O(1)
```python
# Time: O(1), Space: O(1)
def pop_front(head: ListNode | None) -> ListNode | None:
    return head.next if head else None
```

### 3.4 Delete by Value — O(n)
```python
# Time: O(n), Space: O(1)
def erase(head: ListNode | None, target: int) -> ListNode | None:
    dummy = ListNode(0, head)
    prev, cur = dummy, head
    while cur:
        if cur.val == target:
            prev.next = cur.next
            break
        prev, cur = cur, cur.next
    return dummy.next
```

### 3.5 Find (Search) — O(n)
```python
# Time: O(n), Space: O(1)
def find(head: ListNode | None, target: int) -> bool:
    cur = head
    while cur:
        if cur.val == target:
            return True
        cur = cur.next
    return False
```

**Pattern Tip:** Use a **dummy node** for modifications that might touch the head. It removes branching for head/non-head cases.

---

## 4) Two-Pointer Techniques (Fast/Slow)

### 4.1 Find Middle Node — O(n)
```python
# Time: O(n), Space: O(1)
def middleNode(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # middle (for even length, returns second middle)
```

### 4.2 Detect Cycle (Floyd’s Tortoise & Hare) — O(n)
```python
# Time: O(n), Space: O(1)
def hasCycle(head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

### 4.3 Find Cycle Entry — O(n)
```python
# Time: O(n), Space: O(1)
def detectCycle(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            fast = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

### 4.4 Remove N-th From End — O(n)
```python
# Time: O(n), Space: O(1)
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next  # delete
    return dummy.next
```

---

## 5) Reversal Patterns

### 5.1 Reverse Entire List — Iterative — O(n)
```python
# Time: O(n), Space: O(1)
def reverseList(head: ListNode | None) -> ListNode | None:
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

### 5.2 Reverse Sublist `[m..n]` — O(n)
```python
# Time: O(n), Space: O(1)
def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(m - 1):
        prev = prev.next
    # reverse next (n-m+1) nodes
    cur = prev.next
    for _ in range(n - m):
        move = cur.next
        cur.next = move.next
        move.next = prev.next
        prev.next = move
    return dummy.next
```

### 5.3 Reverse Nodes in k-Group — O(n)
```python
# Time: O(n), Space: O(1) (ignoring recursion)
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # helper to check length
    def kth(node: ListNode | None, k: int) -> ListNode | None:
        while node and k:
            node = node.next
            k -= 1
        return node

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth_node = kth(group_prev, k)
        if not kth_node: break
        group_next = kth_node.next
        # reverse group
        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        # reconnect
        tmp = group_prev.next
        group_prev.next = kth_node
        group_prev = tmp
    return dummy.next
```

---

## 6) Merging, Sorting, and Partitioning

### 6.1 Merge Two Sorted Lists — O(n+m)
```python
# Time: O(n+m), Space: O(1)
def mergeTwoLists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

### 6.2 Sort List (Merge Sort on LL) — O(n log n)
```python
# Time: O(n log n), Space: O(log n) recursion stack
def sortList(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head
    # split by mid
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sortList(head)
    right = sortList(mid)
    return mergeTwoLists(left, right)
```

### 6.3 Partition List Around `x` — O(n)
```python
# Time: O(n), Space: O(1)
def partition(head: ListNode, x: int) -> ListNode:
    small = s_tail = ListNode(0)
    big = b_tail = ListNode(0)
    cur = head
    while cur:
        if cur.val < x:
            s_tail.next, s_tail = cur, cur
        else:
            b_tail.next, b_tail = cur, cur
        cur = cur.next
    b_tail.next = None
    s_tail.next = big.next
    return small.next
```

---

## 7) Palindrome Check — O(n)

**Idea:** Find middle, reverse second half, compare halves, (optionally) restore.
```python
# Time: O(n), Space: O(1)
def isPalindrome(head: ListNode | None) -> bool:
    if not head or not head.next: return True
    # find mid
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse second half
    prev, cur = None, slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    # compare
    p1, p2 = head, prev
    ok = True
    while p2:
        if p1.val != p2.val:
            ok = False; break
        p1, p2 = p1.next, p2.next
    # (optional) restore second half
    # ...
    return ok
```

---

## 8) Intersection of Two Linked Lists — O(n+m)

**Two-pointer switching**: Walk A then B, B then A; they meet at intersection or both reach `None`.
```python
# Time: O(n+m), Space: O(1)
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode | None:
    a, b = headA, headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
```

---

## 9) Copy List with Random Pointer — O(n)

### 9.1 HashMap copy (simple) — O(n) space
```python
# Time: O(n), Space: O(n)
class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None):
        self.val = x; self.next = next; self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    if not head: return None
    mp = {}
    cur = head
    while cur:
        mp[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        mp[cur].next = mp.get(cur.next)
        mp[cur].random = mp.get(cur.random)
        cur = cur.next
    return mp[head]
```

### 9.2 Interleaving copy (O(1) extra space)
```python
# Time: O(n), Space: O(1) extra
def copyRandomList_O1(head: 'Node') -> 'Node':
    if not head: return None
    cur = head
    # 1) interleave cloned nodes
    while cur:
        nxt = cur.next
        cur.next = Node(cur.val, next=nxt)
        cur = nxt
    # 2) assign random
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    # 3) separate
    dummy = Node(0)
    copy_tail = dummy
    cur = head
    while cur:
        copy = cur.next
        cur.next = copy.next
        copy_tail.next = copy
        copy_tail = copy
        cur = cur.next
    return dummy.next
```

---

## 10) Design with Linked List: LRU Cache — O(1) Ops

Use **DLL + HashMap** (key → node) for O(1) `get`/`put`. Move recently used nodes to head; evict from tail.
```python
# Time: O(1) per op, Space: O(capacity)
class Node:
    def __init__(self, k=0, v=0):
        self.k, self.v = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}
        self.head = Node(); self.tail = Node()  # sentinels
        self.head.next = self.tail; self.tail.prev = self.head

    def _add_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: Node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _move_front(self, node: Node):
        self._remove(node)
        self._add_front(node)

    def get(self, key: int) -> int:
        if key not in self.mp: return -1
        node = self.mp[key]
        self._move_front(node)
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.v = value
            self._move_front(node)
            return
        node = Node(key, value)
        self.mp[key] = node
        self._add_front(node)
        if len(self.mp) > self.cap:
            # evict from tail
            rm = self.tail.prev
            self._remove(rm)
            del self.mp[rm.k]
```

---

## 11) Advanced Topics (for deeper study)

- **Skip Lists:** probabilistic structure offering O(log n) expected search/insert/delete with layered linked lists.
- **Lock-free Lists:** using atomic CAS operations; hazard pointers/RCU.
- **Persistent Lists:** structural sharing in functional programming (immutability, cons-lists).
- **Sentinel Invariants:** formal reasoning that dummy nodes preserve correctness across edge cases.
- **Memory:** Python uses references/GC; in C/C++ manage allocation/deallocation manually; avoid leaks/dangling pointers.

---

## 12) Edge Cases & Testing Checklist

- `head = None` (empty), single-node, two-nodes
- Operations that affect head/tail
- Duplicates, sorted vs unsorted inputs
- Cycles present/absent
- Very large lists; recursion depth limits (prefer iterative)

---

## 13) LeetCode Problem Map (curated)

Basic:
- **206. Reverse Linked List** — iterative/recursive. (Rev pattern)
- **141. Linked List Cycle** — Floyd detect. (Two-pointer)
- **21. Merge Two Sorted Lists** — merging. (Two pointers)
- **83/82. Remove Duplicates from Sorted List (I/II)** — pointer surgery.

Intermediate:
- **24. Swap Nodes in Pairs** — pointer rewiring (dummy helps).
- **92. Reverse Linked List II** — reverse sublist.
- **160. Intersection of Two LL** — two-pointer switching.
- **234. Palindrome Linked List** — mid + reverse second half.
- **143. Reorder List** — split, reverse second, weave.
- **86. Partition List** — two buckets, concatenate.
- **328. Odd Even Linked List** — stitch odds then evens.
- **61. Rotate List** — connect to cycle, break at k.

Advanced:
- **25. Reverse Nodes in k-Group** — k-chunk reverse.
- **138. Copy List with Random Pointer** — O(1) extra via interleaving.
- **148. Sort List** — merge sort on LL.
- **23. Merge k Sorted Lists** — heap or divide & conquer.
- **146. LRU Cache** — DLL + hashmap design.

---

## 14) Tips, Tricks, and Invariants

- **Dummy nodes** reduce edge-case branching. Always consider starting with `dummy = ListNode(0, head)`.
- Keep a stable naming scheme: `prev`, `cur`, `nxt` (or `next_` to avoid shadowing keyword in some langs).
- After rewiring pointers, **draw** the before/after; ensure no node is lost.
- For compare-type problems (palindrome, intersection), prefer **O(1)** extra via two-pointers/reversal over extra arrays.
- Be wary of recursion depth in Python; prefer iterative where possible for large inputs.

---

## 15) Mini-Exercises

1. Implement `push_back` with a maintained tail pointer in O(1).
2. Write a function to **delete the k-th node** (1-indexed) in O(n) using a dummy head.
3. Given `head`, **split the list** into two halves (first half longer if odd) and return both heads.
4. Implement **circular detection** and return cycle length.
5. Prove that the two-pointer intersection algorithm terminates in at most `len(A)+len(B)` steps.

---

**End of Linked List Notes**
