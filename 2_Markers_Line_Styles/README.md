# Section 2 — Markers, colors, and line styles

This section covers markers (point symbols), line styles, and color customization.

Example:

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10]) # As x points is not mentioned, the default x-values will be 0 to 3. 

# Basic marker
plt.plot(ypoints, marker='X')

# Custom line style, marker face/edge colors, and line color
plt.plot(ypoints, linestyle='dotted', marker='d', markerfacecolor='red', markeredgecolor='green', color='blue')

plt.show()
```

Common markers: 'o' (circle), '*' (star), '.' (point), 'x', 'X', '+', 's' (square), 'D' (diamond)
Line styles: '-' (solid), ':' (dotted), '--' (dashed), '-.' (dash-dot)

