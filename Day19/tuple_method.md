```markdown
## Tuple Methods

As tuples are an immutable type of collection of elements, they have limited built-in methods. They are explained below:

### `count()` Method
The `count()` method of a tuple returns the number of times the given element appears in the tuple.

**Syntax:**
```python
tuple.count(element)
```

**Example:**
```python
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
```

**Output:**
```
Count of 3 in Tuple1 is: 3
```

### `index()` Method
The `index()` method returns the first occurrence of the given element from the tuple.

**Syntax:**
```python
tuple.index(element, start, end)
```

Note: This method raises a `ValueError` if the element is not found in the tuple.

**Example:**
```python
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
```

**Output:**
```
First occurrence of 3 is 3
```
```