**User input** in Python lets the program receive data from the user using the `input()` function.

### Key Points:

1. **Basic Usage**:
   - `input()` gets a string from the user.
   - Example:
     ```python
     name = input("Enter your name: ")
     print("Hello, " + name)
     ```

2. **Convert Input**:
   - Convert to other types if needed.
   - Example:
     ```python
     age = int(input("Enter your age: "))
     ```

3. **Handle Errors**:
   - Use `try-except` for conversion errors.
   - Example:
     ```python
     try:
         age = int(input("Enter your age: "))
     except ValueError:
         print("Invalid number.")
     ```

4. **Prompt Message**:
   - Customize prompts for clarity.
   - Example:
     ```python
     color = input("Favorite color? ")
     print("Your favorite color is " + color)
     ```

### Example:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Name: {name}, Age: {age}")
```

User input allows interaction by getting and processing user data.