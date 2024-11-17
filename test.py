import matplotlib.pyplot as plt
import numpy as np

# Define the function for edge growth based on dimensions
def edges_per_dimension(d):
    if d < 0:
        return 0
    elif d == 0:
        return 0
    else:
        return 2**(d+1) - 2

# Generate x values (dimensions) and corresponding y values (edges)
x_values = np.linspace(-1, 10, 1000)  # Cover negative to find roots
y_values = [edges_per_dimension(x) for x in x_values]

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Edges per Dimension', color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)

# Highlight the roots at (0,0) and beyond
plt.scatter(0, 0, color='red', zorder=5, label='Root at (0, 0)')

# Graph labels and legend
plt.title('Development of Edges by Dimensions')
plt.xlabel('Dimensions (x)')
plt.ylabel('Number of Edges (y)')
plt.legend()
plt.grid(True)
plt.show()
