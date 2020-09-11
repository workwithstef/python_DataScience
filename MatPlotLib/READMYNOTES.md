### MatPlotLib

`from matplotlib import pyplot as plt` - imports pyplot module for use in Python

#### Line Plots

- Creating a simple line graph
- `plt.plot()` - plots specified points
- `plt.show()` - prints graph

Ex.1
```buildoutcfg
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
plt.plot(x_values, y_values)
plt.show()
```
*Simple line graph of y_values against x_values*

Ex.2
```buildoutcfg
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)

plt.show()
```
*Multiple line plots on one graph*

- Lines are customizable.
- Colors, linestyles and markers can be applied using keywords
- Full matplotlib documentation has details on all possible options

Ex.3
```buildoutcfg
plt.plot(time, revenue, color='purple', linestyle='--')
plt.plot(time, costs, color='#82edc9', marker='s')
```

- Zoom in/out of axes using `plt.axis([])`

Syntax: plt.axis([min x-value, max x-value, min y-value, max y-value])

Ex.4

```buildoutcfg
plt.axis([5, 14, 0, 100])
```

*x-axis= 5 to 14, y-axis= 0 to 100*

- Label x-axis & y-axis with `plt.xlabel()` `plt.ylabel()`.
- Title graph with `plt.title()`

Ex.5

```buildoutcfg
plt.xlabel('x_axis label')
plt.ylabel('y_axis label')
plt.title('Title')
```

##### Subplots

When two graphs are plotted side-by-side in the same figure, this is called a subplot

Syntax: plt.subplot(no. of rows, no. of columns, graph index)

Ex.1

```buildoutcfg
# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
```
*Indexing selects the subplots from left-to-right*

Adjusting subplot placement: `.subplots_adjust()`

Keywords:
- `left=` - left side margin
- `right=` - right side margin
- `bottom=` - bottom margin
- `top=` - top margin
- `wspace=` - horizontal space between subplots
- `hspace=` - vertical space between subplots

Ex.2

```buildoutcfg
# Left Plot
plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Right Plot
plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Subplot Adjust
plt.subplots_adjust(wspace=0.35, top=0.2)
```

*increases horizontal space by 0.35 and top margin by 0.2*

Legends: `plt.legend()`

- .legend([]) method takes a list of names for your plots, in order corresponding to the order of each plot.
- Additionally, keyword 'loc' can be used to define where the legend box appears on the graph.

Ex.

```buildoutcfg
plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)
legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']
plt.legend(legend_labels, loc=8)
```
*Different 'loc' numbers (0-10) correspond to a different location*

Alternatively you can specify a legend label in the .plot() method.

Ex.
```buildoutcfg
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16],
         label="parabola")
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64],
         label="cubic")
plt.legend() # Still need this command!
```

Customizing specific subplot axes.

- First save specific plot to a variable - defining an axes object `ax = plt.subplot(1, 2, 1)`
- Now any adjustments specific to that plot can be done using the object

```buildoutcfg
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

plt.plot(months, conversion)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])
```
*In this example, the x & y ticks were defined, then relabelled accordingly using the .set_xticks & .set_xticklabels methods*

*This example mostly demonstrates the xtick/ytick methods but assigning subplots to specific objects can be very useful for separation of concerns*

- `plt.close('all')` - clears all existing plots
- `plt.figure(figsize=(width,height))` - specifies figure size in inches
- `plt.savefig('figure_name.filetype')` - saves figure as specified file format (i.e. pdf, svg, png)