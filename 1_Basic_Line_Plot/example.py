

# Import matplotlib for plotting and numpy for numerical arrays
import matplotlib.pyplot as plt
import numpy as np

# Define x and y data as NumPy arrays
x = np.array([0, 6])  # x coordinates for two points: 0 and 6
y = np.array([10, 250])  # corresponding y coordinates

# Plot y versus x as a line
plt.plot(x, y)  # draws a line connecting (0,10) and (6,250)

# Display the plot window
plt.show()
