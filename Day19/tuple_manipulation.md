```markdown
## Manipulating Tuples

Tuples are immutable; hence if you want to add, remove, or change tuple items, you must first convert the tuple to a list. Then, perform operations on that list and convert it back to a tuple.

### Example:
```python
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item 
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)
```

**Output:**
```
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
```

Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert the list back to a tuple.

However, we can directly concatenate two tuples without converting them to a list.

### Example:
```python
countries = ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
```

**Output:**
```
('Pakistan', 'Afghanistan', 'Bangladesh', 'Sri Lanka', 'Vietnam', 'India', 'China')
```
```