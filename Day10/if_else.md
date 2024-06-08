```markdown
## `if-else` Statements

Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into the following types:

- `if`
- `if-else`
- `if-else-elif`
- Nested `if-else-elif`

### An `if……else` Statement Evaluates Like This:

1. **If the expression evaluates to True:**
   - Execute the block of code inside the `if` statement.
   - After execution, return to the code outside of the `if……else` block.

2. **If the expression evaluates to False:**
   - Execute the block of code inside the `else` statement.
   - After execution, return to the code outside of the `if……else` block.

### Example:

```python
applePrice = 210
budget = 200
if applePrice <= budget:
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```

**Output:**
```
Alexa, do not add Apples to the cart.
```
```