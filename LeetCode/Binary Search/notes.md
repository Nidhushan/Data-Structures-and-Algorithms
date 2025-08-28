# Binary Search — Notes (Kai)

## High-level idea
Binary search is a divide‑and‑conquer technique for finding an index or value by repeatedly halving the search space. It works when the search space is **sorted** or when there is a **monotonic predicate** (false → true only once).

## Why it’s great
- Time: **O(log n)** per search (n = size of search space)
- Space: **O(1)** iterative, **O(log n)** recursive due to call stack
- Deterministic and cache‑friendly

## Core template (index-based, ascending array)
```python
# Time: O(log n), Space: O(1)
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2   # prevents overflow in other languages
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

## Always remember
- Use `mid = l + (r - l) // 2` (safer across languages).
- Choose **invariants** and stick to them (e.g., loop `while l <= r` vs `while l < r`).
- Off‑by‑one mistakes happen at boundaries; draw indices for 3–4 elements to sanity check.

## Variants cheat‑sheet

### 1) **First occurrence (lower_bound)** in a sorted array:
```python
# Time: O(log n), Space: O(1)
def lower_bound(nums, x):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l  # first index i with nums[i] >= x (may be len(nums))
```
**Explanation:**  
The goal of `lower_bound` is to find the first index where the value is **not less than** `x`. It uses a half-open interval `[l, r)` and shrinks the search space based on comparison with `x`.  
- If `nums[mid] < x`, we know the first occurrence must be to the right of `mid`, so we move `l` to `mid + 1`.  
- Otherwise, the first occurrence is at `mid` or to the left, so we move `r` to `mid`.  
The loop continues until `l == r`, which is the position of the first element >= `x`.  

**Example:**  
Given `nums = [1, 2, 4, 4, 5, 7]` and `x = 4`,  
- Initially, `l=0`, `r=6`.  
- Mid indices checked: 3 (value 4), since `nums[3] >= 4`, set `r=3`.  
- Next mid: 1 (value 2), since `2 < 4`, set `l=2`.  
- Next mid: 2 (value 4), since `4 >= 4`, set `r=2`.  
Now `l=2`, `r=2`, loop ends. The first occurrence of 4 is at index 2.

---

### 2) **Upper bound** (first index > x):  
Change the condition to `nums[mid] <= x` then update `l = mid + 1`.  
```python
# Time: O(log n), Space: O(1)
def upper_bound(nums, x):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l  # first index i with nums[i] > x
```
**Example:**  
For `nums = [1, 2, 4, 4, 5, 7]` and `x = 4`, `upper_bound` returns `4` (index of first element > 4, which is 5).

---

### 3) **Peak / unimodal** (e.g., mountain array):  
Compare `nums[mid]` vs `nums[mid+1]` to decide the slope.  
- If `nums[mid] < nums[mid+1]`, the slope is rising, so the peak lies to the right of `mid`. Move `l` to `mid + 1`.  
- Otherwise, the slope is falling or at a peak, so move `r` to `mid`.  

**Example:**  
For `arr = [1, 3, 5, 4, 2]`,  
- At `mid=2` (value 5), compare `arr[2]` and `arr[3]` (5 vs 4), since `5 > 4`, we move `r = mid` (peak is at or before index 2).  
- Eventually, `l` and `r` converge to index 2, the peak.  

This method efficiently finds the peak index in a unimodal array.

---

### 4) **Answer-on-a-number (parametric search):**  
Binary search on the minimal or maximal feasible value, using a monotone predicate `check(v)` that returns `True` if `v` satisfies the condition and `False` otherwise, with the property that if `check(v)` is `True`, then `check(v')` is also `True` for all `v' > v` (monotone increasing).  

**Example:**  
Suppose you want to find the smallest integer `v` such that `v * v >= 20`. Define:  
```python
def check(v):
    return v * v >= 20
```
Using binary search on `v` in `[0, 20]`:  
- If `check(mid)` is `True`, move `r = mid` to find smaller feasible values.  
- Else move `l = mid + 1`.  
Eventually, `l` will be the smallest integer with `v * v >= 20` (which is 5).

---

### EXAMPLE 1 — Search Insert Position (LC 35)
**Task:** Return index of target in sorted array, or the index where it would be inserted to keep order.

**Brute force**
- Scan left→right until `nums[i] >= target`.
- Time: **O(n)**, Space: **O(1)**

**Optimal (lower_bound)**
```python
# Time: O(log n), Space: O(1)
def search_insert(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l
```
**Tips:**
- Use half‑open interval `[l, r)` to avoid `mid±1` noise.
- Works even if `target` is smaller than all or larger than all (returns 0 or n).

---

### EXAMPLE 2 — First and Last Position (LC 34)
**Task:** Find the first and last index of `target` in a sorted array.

**Brute force**
- Linear scan to find first and last.
- Time: **O(n)**, Space: **O(1)**

**Optimal (two binary searches)**
```python
# Time: O(log n), Space: O(1)
def search_range(nums, target):
    def lb(x):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < x:
                l = m + 1
            else:
                r = m
        return l
    left = lb(target)
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    right = lb(target + 1) - 1
    return [left, right]
```
**Tips:**
- `right = lower_bound(target+1) - 1` is a neat trick to get last occurrence.

---

### EXAMPLE 3 — Peak Index in Mountain Array (LC 852)
**Task:** Array increases then decreases; return the peak index.

**Brute force**
- Scan and track the maximum value/index.
- Time: **O(n)**, Space: **O(1)**

**Optimal (binary search on slope)**
```python
# Time: O(log n), Space: O(1)
def peak_index_mountain(arr):
    l, r = 0, len(arr) - 1
    while l < r:                 # invariant: peak in [l, r]
        m = l + (r - l) // 2
        if arr[m] < arr[m + 1]:  # rising slope → peak to the right
            l = m + 1
        else:                    # falling slope or peak at m → move left boundary
            r = m
    return l
```
**Tips:**
- Use `while l < r` and compare `arr[m]` vs `arr[m+1]`.
- Never access out of bounds; ensure `m+1` is valid (loop condition guarantees it).

---

### EXAMPLE 4 — Minimum in Rotated Sorted Array (LC 153)
**Task:** Find the minimum in a rotated increasing array with distinct values.

**Brute force**
- Return `min(nums)`.
- Time: **O(n)**, Space: **O(1)**

**Optimal (binary search on pivot)**
```python
# Time: O(log n), Space: O(1)
def find_min(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] > nums[r]:   # min in (m, r]
            l = m + 1
        else:                   # min in [l, m]
            r = m
    return nums[l]
```
**Tips:**
- Comparing to `nums[r]` is robust; duplicates require a slightly different approach.

---

### EXAMPLE 5 — BS on Answer (Parametric) — Koko Eating Bananas (LC 875)
**Task:** Minimal eating speed `v` such that Koko finishes within `h` hours.

**Brute force**
- Try all speeds from 1 to max(piles) and simulate.
- Time: **O(max(piles) * n)**, Space: **O(1)**

**Optimal (binary search on feasible speed)**
```python
# Time: O(n log maxPile), Space: O(1)
import math

def min_speed(piles, h):
    def ok(v):  # monotone predicate: True → can finish at speed v
        return sum((p + v - 1) // v for p in piles) <= h

    l, r = 1, max(piles)
    while l < r:
        m = l + (r - l) // 2
        if ok(m):
            r = m
        else:
            l = m + 1
    return l
```
**Tips:**
- Identify monotonicity: if speed `v` works, any `v' > v` works.
- Careful with ceilings; use `(p + v - 1) // v` in integers.

---

## Common pitfalls & pro tips
- Decide interval type early: `[l, r]` vs `[l, r)` and stick with it.
- For **first/last occurrence**, use half‑open intervals; the code is cleaner.
- For **rotated arrays**, compare to `nums[r]` (or `nums[l]`) to know which half is sorted.
- For **floating/real answers**, iterate a fixed number of times or until precision met.
- Always prove **loop invariants** to yourself with a tiny example (n=3 or n=4).

## Practice checklist
- [ ] LC 35 Search Insert Position — lower_bound
- [ ] LC 34 First/Last Position — two lower_bounds
- [ ] LC 69 Sqrt(x) — BS on answer
- [ ] LC 852 Peak in Mountain — slope BS
- [ ] LC 153/154 Find Minimum in Rotated — pivot BS
- [ ] LC 33 Search in Rotated — decide which half is sorted
- [ ] LC 875 Koko Bananas — parametric BS

End of notes — keep templates handy and test boundaries (empty array, size 1, all equal, target at ends).
