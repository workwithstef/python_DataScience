### List Comprehension

- Faster, more compact way iterate over a list
- Similar to for loops

E.g
``` 
temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_adjusted = [temp + 20 for temp in temperatures]
# temperatures_adjusted is now [15, 49, 46, 13, 21, 38, 32, 51]
```
In this example, 'temp' denotes each element in the list, 'temp + 20' is the operation, 'temperatures' is the list.

- Every list comprehension has the following syntax ==> ['operation' for 'element' in 'list']

Ex.2
``` 
x_values_1 = [2*index for index in range(5)]
# [0.0, 2.0, 4.0, 6.0, 8.0] 
x_values_2 = [2*index + 0.8 for index in range(5)]
# [0.8, 2.8, 4.8, 6.8, 8.8]

x_values_midpoints = [(x1 + x2)/2.0 for (x1, x2) in zip(x_values_1, x_values_2)]
# [0.4, 2.4, 4.4, 6.4, 8.4]
```

Ex.3
``` 
xy = [[1, 3], [2, 4], [3, 3], [4, 2]]
z = [x * y for (x, y) in xy]
print(z)
# ==> [3, 8, 9, 8]
```

### Lambda Functions

- a lambda function is a one-line shorthand for function
- NOT reusable like normal functions so only good for single-use
- can quickly run an expression and produce an output for a specific task, like defining a column in a table, or populating information in a dictionary.


Ex.1
``` 
add_two = lambda my_input: my_input + 2
print(add_two(3))
# 5
print(add_two(100))
# 102
print(add_two(-2))
# 0
```

Ex.2
``` 
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'
print(check_if_A_grade(91))
# 'Got an A!'
print(check_if_A_grade(70))
# 'Did not get an A...'
print(check_if_A_grade(20))
# 'Did not get an A...'
```

- General lambda syntax:

function_name = lambda 'parameter': 'operation on parameter'

- Lambda syntax for if-statements:

'RETURN IF STATEMENT IS TRUE' if 'IF STATEMENT' else 'RETURN IF STATEMENT IS FALSE'