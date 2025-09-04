# Stack Data Structure Notes

## Introduction

A **stack** is a linear data structure that follows the **Last-In, First-Out (LIFO)** principle. The last element added to the stack is the first one to be removed. Stacks are widely used in algorithms, language parsing, expression evaluation, and backtracking problems.

## Core Concepts

- **LIFO Principle:** The most recently added element is the first to be removed.
- **Push:** Add an element to the top of the stack.
- **Pop:** Remove and return the top element of the stack.
- **Peek/Top:** View the top element without removing it.
- **IsEmpty:** Check if the stack is empty.

**Python Example:**
```python
stack = []
stack.append(1)    # Push
stack.append(2)
top = stack[-1]    # Peek
val = stack.pop()  # Pop
empty = len(stack) == 0  # IsEmpty
# Time: O(1) for push, pop, peek; Space: O(n)
```

## Time and Space Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Push      | O(1)           | O(n)            |
| Pop       | O(1)           | O(n)            |
| Peek      | O(1)           | O(n)            |
| IsEmpty   | O(1)           | O(n)            |

## Example Problems

### 1. Valid Parentheses

**Problem:** Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#### Brute Force Approach
Check all pairs and remove matched pairs repeatedly (inefficient).

#### Optimized with Stack
Use a stack to track opening brackets.
```python
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
# Time: O(n), Space: O(n)
```

### 2. Next Greater Element

**Problem (classic):** Given an array `nums`, for each element find the **next greater element (NGE)** to its right. If none exists, put `-1`.

**Why a stack?** We want, for each index `i`, the first index `j>i` with `nums[j] > nums[i]`. Scanning left→right, a **monotonic decreasing stack of indices** lets us resolve pending elements as soon as we see a larger value.

**Idea/invariant:**
- Maintain a stack of indices whose values are in **strictly decreasing** order (`nums[stack[-1]] > nums[stack[-2]] > ...`).
- When we read a new value `num=nums[i]`, we **pop** all indices on the stack with smaller values; for each popped index `idx`, `nums[i]` is its next greater element.
- Then we **push** `i` (it now waits for someone larger to the right).

**Algorithm (optimized with monotonic stack):**
```python
# Time: O(n)  (each index is pushed and popped at most once)
# Space: O(n) for the stack and result array

def nextGreater(nums):
    n = len(nums)
    res = [-1] * n
    st = []  # stack of indices; nums[st] is strictly decreasing
    for i, x in enumerate(nums):
        # Resolve all smaller elements waiting on the stack
        while st and nums[st[-1]] < x:
            j = st.pop()
            res[j] = x
        st.append(i)
    return res
```

**Dry run (example `nums = [2, 1, 2, 4, 3]`):**
- i=0, x=2: stack=[] → push 0 → stack=[0]
- i=1, x=1: nums[0]=2 ≥ 1 → push 1 → stack=[0,1]
- i=2, x=2: pop while nums[top] < 2 → pop 1 → res[1]=2; nums[0]=2 !< 2 → stop; push 2 → stack=[0,2]
- i=3, x=4: pop 2 → res[2]=4; pop 0 → res[0]=4; push 3 → stack=[3]
- i=4, x=3: nums[3]=4 ≥ 3 → push 4 → stack=[3,4]
- end → res=[4,2,4,-1,-1]

**Common variations:**
- **Circular array** (e.g., LC 503 Next Greater Element II): simulate two passes by iterating `2*n` and using `nums[i % n]` while only filling answers for `i < n`.
- **Next greater element on a subset** (LC 496): build NGE for the big array once; answer queries by lookup.
- **Daily Temperatures** (LC 739): same pattern; store indices and compare temperatures.
- **Next smaller element**: flip the comparison to build a monotonic **increasing** stack.

**Brute force (for contrast):** For each `i`, scan `j=i+1..n-1` to find the first `nums[j] > nums[i]`.  
Time: O(n²), Space: O(1).

**Pitfalls & tips:**
- Store **indices** on the stack, not values, so you can write into `res` at the correct position.
- Keep the stack **strictly** monotonic (use `<` not `<=`) to avoid infinite loops and ensure correctness when duplicates appear.
- For circular variants, don’t overwrite an already-set answer on the second pass.

**LeetCode practice (in increasing breadth):**
- 496. Next Greater Element I — build NGE for `nums2`, answer queries for `nums1`.  
- 503. Next Greater Element II — circular array version.  
- 739. Daily Temperatures — next warmer day.  
- 901. Online Stock Span — span using a monotonic stack.  
- 84. Largest Rectangle in Histogram — next smaller on both sides (monotonic stack).  
- 85. Maximal Rectangle — builds on 84 with row-wise histograms.

## Common Stack Patterns

- **Monotonic Stack:**  
  A monotonic stack is a stack that maintains its elements in either strictly increasing or strictly decreasing order. This property allows it to efficiently solve problems involving "next greater" or "next smaller" elements by enabling quick access to relevant elements without scanning the entire array repeatedly.

  **Types:**
  - *Increasing Monotonic Stack:* Elements are in increasing order from bottom to top. Used to find next smaller elements.
  - *Decreasing Monotonic Stack:* Elements are in decreasing order from bottom to top. Used to find next greater elements.

  **Why it’s useful:**  
  Monotonic stacks help reduce the time complexity of problems that would otherwise require nested loops (O(n²)) to O(n) by maintaining a stack of candidate elements and resolving queries as new elements are processed.

  **General Algorithm Template:**
  ```python
  def monotonic_stack(arr):
      stack = []
      result = [default_value] * len(arr)  # depends on problem
      for i, val in enumerate(arr):
          while stack and compare(arr[stack[-1]], val):
              idx = stack.pop()
              result[idx] = val  # or other logic based on problem
          stack.append(i)
      return result
  ```
  - `compare` is a comparison function defining the monotonicity (e.g., `<` for strictly increasing, `>` for strictly decreasing).
  - The stack stores indices to allow updating the result array at correct positions.

  **Time Complexity:** O(n)  
  Each element is pushed and popped at most once.

  **Space Complexity:** O(n)  
  For the stack and the result array.

  **Example Dry Run (Next Greater Element):**  
  For `arr = [2, 1, 2, 4, 3]` using a decreasing monotonic stack:
  - i=0, val=2: stack empty → push 0 → stack=[0]
  - i=1, val=1: 2 > 1 → push 1 → stack=[0,1]
  - i=2, val=2: pop while top < 2 → pop 1 → res[1]=2; top now 0 with val=2 not less than 2 → stop; push 2 → stack=[0,2]
  - i=3, val=4: pop 2 → res[2]=4; pop 0 → res[0]=4; push 3 → stack=[3]
  - i=4, val=3: 4 > 3 → push 4 → stack=[3,4]
  - End: positions in stack have no next greater → res = [4,2,4,-1,-1]

  **Common Problems Using Monotonic Stacks:**
  - Next Greater Element I & II (LC 496, 503)
  - Daily Temperatures (LC 739)
  - Online Stock Span (LC 901)
  - Largest Rectangle in Histogram (LC 84)
  - Maximal Rectangle (LC 85)
  - Trapping Rain Water (LC 42)
  - Sliding Window Maximum (LC 239) — uses a deque variant

- **Parentheses/Bracket Matching:** Push opening brackets, pop and check for matching closing brackets.
- **Expression Evaluation:** Convert infix to postfix, evaluate postfix expressions.
- **Min Stack:** Stack supporting retrieving the minimum element in O(1) time.

**Min Stack Example:**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]
# All operations: O(1) time, O(n) space
```

## Tips & Tricks

- Use Python's `list` as a stack (`append`, `pop`).
- For fixed-size or thread-safe stacks, use `collections.deque` or `queue.LifoQueue`.
- When solving problems, look for:
  - "Previous/Next Greater/Smaller" elements
  - Balanced parentheses/brackets
  - Undo operations (backtracking)
  - Function call stacks/recursion simulation
- In many problems, a stack can replace recursion for iterative solutions.

## Summary

- Stacks are simple but powerful for a wide range of problems.
- Key operations (`push`, `pop`, `peek`) are O(1).
- Common in parsing, backtracking, and "next/previous" element problems.
- Mastering stack patterns (like monotonic stack) is essential for efficient algorithms.