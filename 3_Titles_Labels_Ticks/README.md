# Section 3 — Titles, labels, and ticks

This section explains how to add a title, axis labels, and control tick locations. It also shows plotting multiple series on the same axes.


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15,25,30,20]) # First line
y2 = np.array([17,23,38,5])  # Second line
y3 = np.array([13,15,20,30])  # Third line

plt.title("Class size over the years", fontsize=20, family="serif", fontweight="bold") # fontweight = "bold" sets the title to bold highlighting. 
plt.xlabel("Year", fontsize=15) # size of font is 15
plt.ylabel("Class size", fontsize=15)

plt.xticks(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
```
