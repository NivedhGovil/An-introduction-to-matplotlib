# Section 1 — Basic line plot

This section shows how to plot y versus x graph. 

Example: 

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6]) # An array(list)
y = np.array([10, 250])

plt.plot(x, y)
plt.show()
```

Notes:
- If you only pass y values to plt.plot, Matplotlib will assume x = [0, 1, 2, ...].
- Use plt.show() to display the figure. 
