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

### Pandas

To use pandas you must first import the pandas module in Python

```buildoutcfg
import pandas as pd
```

#### DataFrames

- DataFrames are tables containing data in columns and rows.
- Strings, integers, floats, lists, tuples, etc can be passed as row data
- Dictionaries can be passed in also; the key is the column name, and the value is the row data associated to that column

Ex.1 
```buildoutcfg
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)
``` 
*This will produce a table with the three column names and column data shown in each list.*

*(Every column must have equal number of column values or you will get an error)* 

- Lists of lists can be passed in directly. This can fill an entire row, spanning multiple columns.
- Use keyword argument `columns` to pass a list of corresponding column names
- Similar to the INSERT method in SQL.

Ex.2

```buildoutcfg
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
    'Store ID', 'Location', 'Number of Employees'
  ])

print(df2)
```
*The 1st list of lists denotes the row data. Then the 2nd list, keyword 'columns' denotes the corresponding column names*


CSV - Comma-Separated Values

Most DataFrames are pre-existing and are exported/imported as a .csv file

- `.read_csv('filename.csv')` method is used to load DataFrame 
- `.to_csv('new-filename.csv')` method is used to save data to CSV
- `.head()` method is used to print first 5 rows of any DataFrame. `.head(n)` will print 'n' rows of DF.

##### Selecting Columns
Say we want to select a single column of data for boxplot/histogram. 
There's two ways:
- Dictionary-style method; `DF_name['column_name']`
- Or dot method, `DF_name.column_name`; dot method only works if column name follows good variable naming conventions (no spaces/special characters, does not start with a number, etc)

The result of this column data selection is called a 'Series'

To select multiple columns of data, with the Dictionary-style, pass a list of column names as the index. E.g. `DF_name[['column1', 'column2']]`

Since this results in an array (not a single column or single row) it is a DataFrame, not a Series

##### Selecting Rows
`.iloc[n]` dot method, 

To select a single row:
- `DF_name.iloc[2]` this will select 3rd row (zero-indexed)

To select multiple rows:
- `DF_name.iloc[3:7]` 4th to 7th row (3rd up to but not including 7th index) 
- `DF_name.iloc[:3]` all rows up to 3rd row (all up to but not including 3rd index)
- `DF_name.iloc[-3:]` from the 3rd to last row up to the final row

To select rows using logic:
- `DF_name[DF_name.age == 23]` rows where age is 23
- `DF_name[DF_name.age < 73]` rows where age less than 73
- `DF_name[DF_name.city != 'London']` rows where city is not London
- and so on

`&` = "AND" and `|` = "OR"; so statements can be combined.
- `DF_name[(DF_name.city != 'France') & (DF_name.age == 23)]` 23 and not in France

`.isin()` used to check for multiple values of one key
- `DF_name[DF_name.city.isin(['London', 'Brazil', 'Germany'])]` 

##### Setting Indices

Selecting rows using logic results in a jumbled index order.

Can reset DataFrame indices using `df.reset_index()`
This will move old index order to new column; unless `df.reset_index(drop=True)` is used, which will remove them completely.
 
 
##### Modifying Columns

- `df['new_column'] = ['val1', 'val2', 'val3']` - adds new column and corresponding values directly

- `df['VAT'] = df.Price * 0.20` - adds new VAT column and fills rows based on function

`.apply()` method used to quickly apply function to all values of a column

Ex.1 `df.Name.apply(upper)` --> makes all values uppercase

Ex.2 Applying lambda functions to column

```buildoutcfg
get_last_name = lambda val:val.split(' ')[-1]

df['last_name'] = df.name.apply(get_last_name)
```
*This lambda function splits any string at the space and returns the last item of the resultant list.
Then the function is applied to the 'name' column of the DataFrame, the result is applied to the column values of new 'last_name' column*

##### Applying Lambda to a Row

`row.column_name` or `row['column_name']` accesses particular values of a row

```buildoutcfg
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)
```

*In this case, the lambda function calculates total earnings per hours worked, considering how overtime affects hourly rates.
Multiple columns are being incorporated into the function, so when the apply() method is called, keyword 'axis=1' must be used
Furthermore, since more than one column is in play, do not specify a single column when calling .apply()*

##### Renaming Columns

`df.columns` - used to rename all columns
`df.rename` - used to rename single column

Ex.1 Renaming all columns
```buildoutcfg
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
```
*Must list out new names for all columns*

Ex.2 Renaming specific column(s)
```buildoutcfg
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)
```
*Here the 'name' & 'age' column have been changed to 'First Name' & 'Age' respectively.
'inplace=True' keyword is used so the changes are applied to the original DF, instead of making a brand new one*


#### Aggregates

- `.median()` - finds median of integers in a column
- `.nunique()` - counts how many DISTINCT entries in a column
- `.unique()` - lists DISTINCT entries in a column
- `.count()` - counts entries
- `.max()` `.min()` - max/min value
- `.mean()` `.std()` - mean/standard deviation
- and more

##### Grouping

- `.groupby('column value')` - groups specific column value and corresponding row values where operations can be applied; exactly like SQL GROUPBY

Ex.1

```buildoutcfg
orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max()
```
*In this example the distinct shoe_type entries are grouped, and the maximum price for each shoe_type is returned.*

*The result is type '.Series', not a '.DataFrame'*

- .groupby() jumbles the indexing so its good practice to end with .reset_index(). This also transforms your result into a DataFrame, moving the indices into their own column.


Can still apply lambda functions on aggregates. For example:

Ex.2
```buildoutcfg
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
```

*Here a lambda function is applied which calculates the 25th percentile of prices of each shoe_color*
*(Note: numpy module was imported, which is used for the percentile calculation `import numpy as np`)*

- Can group multiple columns by passing a list in the .groupby([]) method

Ex.3

```buildoutcfg
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
```
*This counts the total amount of entries for each shoe type and shoe color.*

##### Pivot Tables

Pivoting is used when grouping multiple columns. It is useful for displaying the resultant DF in a cleaner way.

When you group two columns, (like in Ex.3), the result is the two columns with the chosen aggregate values.
Pivoting takes one of those columns and inverts it into a row, transforming the column values into column headers, resulting in a x-axis/y-axis style DF.
The result is called a pivot table.

Syntax for Pivoting:

```buildoutcfg
df.pivot(
         columns='ColumnToPivot', #x-axis
         index='ColumnToBeRows', #y-axis
         values='ColumnToBeValues' #values
)
```
*(Still follow up with .reset_index() to clean up indexing)*