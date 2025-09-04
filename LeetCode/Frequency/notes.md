# Frequency / Hashing Problems

LC 442

## Introduction to Frequency/Hashmap Technique

Frequency and hashing techniques are fundamental tools for solving a wide variety of problems involving counting occurrences of elements, grouping elements by similarity, or quickly checking membership. They leverage data structures like hash maps (dictionaries in Python) to store and retrieve frequency counts efficiently.

Common use cases include:
- Counting occurrences of characters or elements
- Finding majority elements or top-k frequent elements
- Grouping anagrams or similar items
- Sliding window problems involving frequency constraints

## Core Concepts

### Counting Elements
- Use a dictionary (`dict`) or `collections.Counter` to maintain counts of elements.
- Keys represent the element, values represent the count.
- For small fixed ranges (e.g., only lowercase letters), an array can be used for counting frequencies.

### `collections.Counter`
- Specialized dictionary subclass for counting hashable objects.
- Supports methods like `.most_common()`, which is useful for top-k frequency problems.

### Dictionary (`dict`)
- General-purpose hash map.
- Flexible for any hashable keys.
- Allows incrementing counts as you iterate over elements.

### Array for Small Ranges
- If the input domain is limited (e.g., 'a' to 'z'), use a fixed-size array for counts.
- More space-efficient and faster than dict in such cases.

## Time and Space Complexities

| Operation                      | Time Complexity    | Space Complexity   |
|-------------------------------|--------------------|--------------------|
| Building frequency map         | O(n)               | O(k) (unique keys) |
| Lookup/Increments in dict      | O(1) average       | -                  |
| Sorting frequencies (for top-k)| O(k log k)         | O(k)               |
| Sliding window with freq map   | O(n)               | O(k)               |

- `n` = size of input
- `k` = number of unique elements

## Example Problems

### 1. Valid Anagram

Check if two strings are anagrams by comparing frequency counts.

```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

**Complexity:**  
- Time: O(n)  
- Space: O(1) (since character set is limited)

---

### 2. Majority Element

Find the element that appears more than `n/2` times.

```python
def majorityElement(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num
```

**Complexity:**  
- Time: O(n)  
- Space: O(k)

---

### 3. Top K Frequent Elements

**Problem Statement:**  
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in the array.

**Brute Force Approach:**  
Count the frequency of all elements using a dictionary or Counter, then sort the elements based on their frequency in descending order, and finally return the top `k` elements. This approach requires sorting all unique elements, which can be costly if there are many unique elements.

**Optimized Approach:**  
Use `collections.Counter` to count frequencies, then use a heap (priority queue) to efficiently retrieve the top `k` elements. The `heapq.nlargest` function can be used to get the k elements with the highest frequency without sorting the entire list.

**Dry Run Example:**  
Consider `nums = [1,1,1,2,2,3]` and `k = 2`.  
- Frequency count: `{1: 3, 2: 2, 3: 1}`  
- Using a heap, retrieve the two elements with highest frequency: `[1, 2]`.

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

**Complexity:**  
- Time: O(n + k log n)  
- Space: O(n)

---

### 4. Group Anagrams

**Problem Statement:**  
Given an array of strings, group the strings that are anagrams of each other.

**Why Sorted Word or Frequency Tuple as Key?**  
Anagrams have the same characters in the same frequency, just arranged differently. Sorting each word or using a tuple of character counts provides a unique and consistent key for all anagrams, allowing them to be grouped together.

**Brute Force Approach:**  
Compare every pair of strings to check if they are anagrams, which leads to O(n² * m) time complexity (n = number of strings, m = max length of string).

**Optimized Approach Using defaultdict:**  
Use a dictionary where the key is the sorted string (or frequency tuple) and the value is a list of strings that match the key. This groups all anagrams together efficiently.

**Dry Run Example:**  
Consider `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`.  
- Sort each string: `"eat" -> "aet"`, `"tea" -> "aet"`, `"tan" -> "ant"`, etc.  
- Group by sorted key:  
  - `"aet"`: ["eat", "tea", "ate"]  
  - `"ant"`: ["tan", "nat"]  
  - `"abt"`: ["bat"]

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

**Complexity:**  
- Time: O(n * m log m) (n = number of strings, m = max length)  
- Space: O(n * m)

## Brute Force vs Optimized Solutions

- **Brute Force:** Often involves nested loops to compare elements or count frequencies repeatedly, leading to O(n²) or worse.
- **Optimized:** Use hash maps to count frequencies in O(n), then apply sorting or heap operations to find required results efficiently.

Example:  
- Brute force anagram check: compare every character count manually for each pair → O(n² * m)  
- Optimized: Use frequency maps or sorted keys → O(n * m log m)

## Common Patterns

### Character Counts
- Use frequency maps to count characters.
- Useful in anagram, palindrome, and substring problems.

### Sliding Window + Frequency
- Maintain a window and track frequencies inside it.
- Adjust window size or position based on frequency conditions.
- Example: Longest substring with at most k distinct characters.

### Prefix Sums with Hashmap
- Store prefix frequency sums in a hashmap to quickly find subarrays with certain properties.
- Example: Subarray sum equals k.

### Frequency Sorting
- Sort elements by their frequency using Counter and sorting or heaps.
- Useful in top-k frequent elements problems.

## Tips & Tricks

- Use `collections.Counter` for quick frequency counts.
- For fixed character sets, consider using arrays instead of dicts.
- When grouping anagrams, use sorted strings or character count tuples as keys.
- Sliding window problems often combine frequency maps with two pointers.
- For top-k problems, heaps provide efficient selection.
- Remember to handle edge cases like empty inputs or ties in frequency.

## Summary

- Frequency and hashing techniques are versatile and powerful for counting and grouping problems.
- Using hash maps or counters allows O(n) time frequency computations.
- Combining frequency maps with sorting, heaps, or sliding windows unlocks solutions to many classic problems.
- Understanding and practicing these patterns is essential for efficient problem-solving in coding interviews and algorithm challenges.
