```markdown
## Function Arguments and Return Statement

There are four types of arguments that we can provide in a function:

1. Default Arguments
2. Keyword Arguments
3. Variable-length Arguments
4. Required Arguments

### Default Arguments

We can provide a default value while creating a function. This way, the function assumes a default value even if a value is not provided in the function call for that argument.

#### Example

```python
def name(fname, mname="John", lname="Watson"):
    print("Hello,", fname, mname, lname)

name("Amy")
```

#### Output

```
Hello, Amy John Watson
```

### Keyword Arguments

We can provide arguments with `key = value`. This way, the interpreter recognizes the arguments by the parameter name. Hence, the order in which the arguments are passed does not matter.

#### Example

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname="Peter", lname="Wesker", fname="Jade")
```

#### Output

```
Hello, Jade Peter Wesker
```

### Required Arguments

If we don’t pass the arguments with a `key = value` syntax, then it is necessary to pass the arguments in the correct positional order, and the number of arguments passed should match the actual function definition.

#### Example 1: When the number of arguments passed does not match the actual function definition

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
```

#### Output

```
TypeError: name() missing 1 required positional argument: 'lname'
```

#### Example 2: When the number of arguments passed matches the actual function definition

```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
```

#### Output

```
Hello, Peter Ego Quill
```

### Variable-length Arguments

Sometimes, we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments. There are two ways to achieve this:

#### Arbitrary Arguments

While creating a function, pass a `*` before the parameter name. The function accesses the arguments by processing them as a tuple.

##### Example

```python
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
```

##### Output

```
Hello, James Buchanan Barnes
```

#### Keyword Arbitrary Arguments

While creating a function, pass `**` before the parameter name. The function accesses the arguments by processing them as a dictionary.

##### Example

```python
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")
```

##### Output

```
Hello, James Buchanan Barnes
```

## Return Statement

The `return` statement is used to return the value of the expression back to the calling function.

#### Example

```python
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
```

#### Output

```
Hello, James Buchanan Barnes
```
```