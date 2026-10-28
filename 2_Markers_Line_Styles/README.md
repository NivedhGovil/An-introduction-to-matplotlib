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

# Common Markers

| Symbol / Code | Description |
| :--- | :--- |
| `o` | Circle |
| `*` | Star |
| `.` | Point |
| `x` | Cross (`x`) |
| `X` | Uppercase Cross (`X`) |
| `+` | Plus |
| `s` | Square |
| `D` | Diamond |

### Line Styles

| Symbol / Code | Style |
| :--- | :--- |
| `-` | Solid |
| `:` | Dotted |
| `--` | Dashed |
| `-.` | Dash-dot |

