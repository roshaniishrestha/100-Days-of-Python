String slicing in Python allows you to access a portion of a string (substring) using a specified range of indices. This is done using the slice notation: `string[start:stop:step]`.

### Basic Syntax

- `start`: The starting index of the substring (inclusive).
- `stop`: The ending index of the substring (exclusive).
- `step`: The step size or interval between characters.

### Examples

1. **Basic Slicing**:
   - Access a substring from index `start` to `stop - 1`.
   - Example:
     ```python
     text = "Hello, World!"
     print(text[0:5])  # Output: Hello
     ```

2. **Omitting Indices**:
   - Omitting `start` defaults to `0`.
   - Omitting `stop` defaults to the end of the string.
   - Example:
     ```python
     print(text[:5])   # Output: Hello
     print(text[7:])   # Output: World!
     ```

3. **Negative Indices**:
   - Use negative indices to count from the end of the string.
   - Example:
     ```python
     print(text[-6:])  # Output: World!
     print(text[:-7])  # Output: Hello,
     ```

4. **Step Size**:
   - Use the `step` parameter to skip characters.
   - Example:
     ```python
     print(text[::2])  # Output: Hlo ol!
     print(text[1::2]) # Output: el,Wrd
     ```

5. **Reversing a String**:
   - Use a negative `step` to reverse the string.
   - Example:
     ```python
     print(text[::-1]) # Output: !dlroW ,olleH
     ```

### Examples in Action

```python
text = "Python Programming"

# Basic slicing
print(text[0:6])  # Output: Python

# Omitting start and stop
print(text[:6])   # Output: Python
print(text[7:])   # Output: Programming

# Negative indices
print(text[-11:])  # Output: Programming
print(text[:-12])  # Output: Python

# Step size
print(text[0:12:2]) # Output: Pto rg

# Reversing a string
print(text[::-1])   # Output: gnimmargorP nohtyP
```

### Summary

- String slicing is a powerful feature that allows for flexible access to substrings.
- The `start`, `stop`, and `step` parameters can be used in various combinations to achieve the desired slicing.
- Negative indices and step sizes offer additional control for slicing and reversing strings.