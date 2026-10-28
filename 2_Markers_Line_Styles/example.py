import matplotlib.pyplot as plt
import numpy as np

# Example data
ypoints = np.array([3, 8, 1, 10])

# Plot with a filled X marker at each data point.
plt.plot(ypoints, marker='X')  # marker='X' draws a large filled X on each point. One method to plot the graph. 

# Plot again (on the same axes) with more customization
plt.plot(
    ypoints,
    linestyle='dotted',            # dotted line style
    marker='d',                    # diamond marker for each data point
    markerfacecolor='red',         # fill color of the marker
    markeredgecolor='green',       # marker border color
    color='blue'                   # line color
)

plt.show()
