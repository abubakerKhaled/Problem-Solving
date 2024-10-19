# The Optimal Solution for problem 15

This is the optimal solution for String Compression problem
This is the old solution

```python
class Solution:
    def compress(self, chars: list[str]) -> int:
        result = ""
        curr = 0
        count = 0
        next = 1
        while curr < len(chars):
            if next < len(chars) and chars[curr] == chars[next]:
                next += 1
                count += 1
            else:
                count += 1
                result += chars[curr]
                if count > 1:
                    result += str(count)
                count = 0
                curr = next
                next += 1
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)
```

## Current Solution Breakdown

- **Space Complexity**: The current solution builds a new string `result` to store the compressed characters, then copies it back to the `chars` array. This increases the space complexity to O(n) due to the use of the `result` string.
- **Time Complexity**: The time complexity is O(n), which is optimal in terms of iterating through the list, but there are some redundant steps in copying the `result` string back to `chars`.

## Optimized Approach

Instead of building a new string, we can perform the compression **in-place** by modifying the `chars` array directly. This will eliminate the need for an additional `result` string, reducing the space complexity to O(1) (excluding the input size). We can also simplify the logic slightly to avoid managing two separate pointers (`curr` and `next`).

## Optimized Solution

```python
class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0

        write = 0  # position to write compressed characters
        read = 0   # position to read characters

        while read < n:
            char = chars[read]
            count = 0
            
            # Count how many times the current character repeats
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the array
            chars[write] = char
            write += 1

            # If the character repeats, write the count
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
```

### Key Changes

1. **In-place compression**: Instead of building a `result` string, we modify the `chars` array directly. We use a `write` pointer to keep track of where to write the compressed characters.
2. **Simplified iteration**: Instead of managing two pointers (`curr` and `next`), we use just one `read` pointer to scan the characters. We calculate the count of repeated characters while moving the `read` pointer and write the result as we go.
3. **Writing the count**: If a character is repeated, we convert the count to a string and write each digit in the `chars` array.

### Time Complexity

- **Time Complexity**: O(n), since we still iterate through the entire list once.
- **Space Complexity**: O(1) (ignoring input size), as no extra space is used beyond the input list.

### Example Run

For input `["a", "a", "b", "b", "c", "c", "c"]`, the in-place modification will work as follows:

- Write `'a'` and `2` to the first two positions.
- Write `'b'` and `2` to the next two positions.
- Write `'c'` and `3` to the next two positions.
  
The final array will be `["a", "2", "b", "2", "c", "3"]`, and the function will return `6` as the compressed length.
