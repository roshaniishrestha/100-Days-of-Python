```markdown
## `elif` Statements

Sometimes, the programmer may want to evaluate more than one condition; this can be done using an `elif` statement.

### Working of an `elif` Statement

1. **Execute the block of code inside the `if` statement if the initial expression evaluates to True.**  
   After execution, return to the code outside of the `if` block.

2. **Execute the block of code inside the first `elif` statement if the expression inside it evaluates to True.**  
   After execution, return to the code outside of the `if` block.

3. **Execute the block of code inside the second `elif` statement if the expression inside it evaluates to True.**  
   After execution, return to the code outside of the `if` block.

4. **Continue this pattern for subsequent `elif` statements:**  
   Execute the block of code inside the nth `elif` statement if the expression inside it evaluates to True. After execution, return to the code outside of the `if` block.

5. **Execute the block of code inside the `else` statement if none of the expressions evaluates to True.**  
   After execution, return to the code outside of the `if` block.

### Example:

```python
num = 0
if num < 0:
    print("Number is negative.")
elif num == 0:
    print("Number is Zero.")
else:
    print("Number is positive.")
```

**Output:**
```
Number is Zero.
```
```