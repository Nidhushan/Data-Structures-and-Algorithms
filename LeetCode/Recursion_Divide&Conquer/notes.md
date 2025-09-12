# Recursion & Divide-and-Conquer

## Introduction
Recursion is a fundamental programming technique where a function calls itself to solve smaller instances of the same problem. Divide-and-Conquer is a powerful algorithmic paradigm that breaks a problem into subproblems, solves them (often recursively), and then combines their results.

---

## Key Concepts
- **Base Case**: The simplest instance of the problem, where recursion stops.
- **Recursive Case**: The part of the function where it calls itself with smaller or simpler inputs.
- **Recursion Tree**: A conceptual diagram that visualizes recursive calls as a tree, useful for understanding time complexity.
- **Recurrence Relations**: Mathematical equations describing the overall time complexity based on the subproblems (e.g., T(n) = 2T(n/2) + O(n)).
- **Space Complexity (Stack Frames)**: Each recursive call adds a new stack frame; deep recursion can cause stack overflow. Space complexity is often proportional to the maximum depth of recursion.

---

## Divide-and-Conquer vs. Plain Recursion
- **Plain Recursion**: Solves a problem by breaking it into one or more subproblems, not necessarily dividing the size (e.g., Fibonacci).
- **Divide-and-Conquer**: Always divides the problem into smaller, usually equal-sized subproblems, solves them recursively, and combines the results (e.g., Merge Sort, Quick Sort).

| Aspect                | Plain Recursion            | Divide-and-Conquer           |
|-----------------------|---------------------------|------------------------------|
| Subproblem Size       | May not decrease by much  | Typically halves/subdivides  |
| Combination Phase     | Often trivial             | Explicit combine/merge step  |
| Examples              | Factorial, Fibonacci      | Merge Sort, Quick Sort       |

---

## Tips & Tricks
- Always define clear base cases to avoid infinite recursion.
- Use memoization to optimize overlapping subproblems (Dynamic Programming).
- For large input sizes, consider tail recursion or iterative approaches to avoid stack overflow.
- Draw the recursion tree for complex recursions to analyze time complexity.
- Use helper functions for passing extra parameters (e.g., current path, index).

---

## Common Mistakes
- Missing or incorrect base case(s).
- Infinite recursion due to improper input reduction.
- Not combining results correctly in divide-and-conquer.
- Stack overflow due to excessive recursion depth.
- Not considering time/space complexity.

---

## Sample Code Examples

### 1. Factorial (Plain Recursion)
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### 2. Fibonacci (Plain Recursion & Memoization)
```python
# Plain recursion (exponential time)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# With memoization (linear time)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

### 3. Merge Sort (Divide-and-Conquer)
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 4. Quick Sort (Divide-and-Conquer)
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

### 5. Subsets (Backtracking/Recursion)
```python
def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res
```

### 6. Generate Parentheses (Backtracking/Recursion)
```python
def generateParenthesis(n):
    res = []
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    backtrack()
    return res
```

### 7. Maximum Subarray (Divide-and-Conquer)
```python
def maxSubArray(nums):
    def helper(left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_sum = helper(left, mid)
        right_sum = helper(mid+1, right)
        cross_sum = maxCrossingSum(nums, left, mid, right)
        return max(left_sum, right_sum, cross_sum)
    def maxCrossingSum(nums, left, mid, right):
        left_max = float('-inf')
        curr = 0
        for i in range(mid, left-1, -1):
            curr += nums[i]
            left_max = max(left_max, curr)
        right_max = float('-inf')
        curr = 0
        for i in range(mid+1, right+1):
            curr += nums[i]
            right_max = max(right_max, curr)
        return left_max + right_max
    return helper(0, len(nums)-1)
```

---

## When to Use Recursion vs Iterative Approaches
- Use recursion for problems naturally defined in terms of subproblems (e.g., tree traversals, combinatorial generation).
- Use iterative solutions when recursion depth may be large or stack overflow is a concern.
- Sometimes, recursion is clearer and more concise, but iterative solutions may be more efficient in time/space.
- For dynamic programming, recursion + memoization (top-down) and iterative DP (bottom-up) are often interchangeable.

---

## Advanced Extensions
- **Backtracking**: Recursion with state undoing, used for combinatorial search (e.g., permutations, N-Queens).
- **Dynamic Programming (DP)**: Recursion + memoization to avoid redundant computations.
- **Recursion + Binary Search**: Recursive binary search, or divide-and-conquer for problems like "search in a rotated array".
- **Tail Recursion**: Some languages optimize tail calls, but Python does not.

---

## Curated Problem List (LeetCode)

### Basic
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) √
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) √
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) √
- [231. Power of Two](https://leetcode.com/problems/power-of-two/) √
- [326. Power of Three](https://leetcode.com/problems/power-of-three/) √
- [342. Power of Four](https://leetcode.com/problems/power-of-four/) √
- [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) √
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) √
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
- [112. Path Sum](https://leetcode.com/problems/path-sum/)
- [617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

### Intermediate
- [46. Permutations](https://leetcode.com/problems/permutations/)
- [78. Subsets](https://leetcode.com/problems/subsets/)
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

### Advanced
- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)
- [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)
- [51. N-Queens](https://leetcode.com/problems/n-queens/)
- [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
- [282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

---