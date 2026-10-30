import matplotlib.pyplot as plt
import numpy as np

# Simple x and two y-series
x = np.array([0, 1, 2, 3, 4])
y1 = np.array([1, 4, 9, 16, 25])
y2 = np.array([1, 2, 3, 4, 5])

# fmt shorthand: marker|line|color
plt.plot(x, y1, '*--y')  # star markers, dashed line, yellow color
plt.plot(x, y2, 'o-')    # circle markers, solid line

plt.show()
