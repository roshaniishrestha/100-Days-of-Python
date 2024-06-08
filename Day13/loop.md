```markdown
# Introduction to Loops

Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this, loops are further classified into the following main types:

- `for` loop
- `while` loop

## The `for` Loop

`for` loops can iterate over a sequence of iterable objects in Python. Iterating over a sequence means iterating over strings, lists, tuples, sets, and dictionaries.

### Example: Iterating over a string

```python
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```

**Output:**
```
A, b, h, i, s, h, e, k,
```

### Example: Iterating over a list

```python
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```

**Output:**
```
Red
Green
Blue
Yellow
```

Similarly, we can use loops for sets and dictionaries.

## `range()`

What if we do not want to iterate over a sequence? What if we want to use a `for` loop for a specific number of times?

Here, we can use the `range()` function.

### Example:

```python
for k in range(5):
    print(k)
```

**Output:**
```
0
1
2
3
4
```

Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also loop over a specific range.

### Example:

```python
for k in range(4, 9):
    print(k)
```

**Output:**
```
4
5
6
7
8
```

## Quick Quiz

Explore the third parameter of `range` (i.e., `range(x, y, z)`).
```