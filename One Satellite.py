import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define parameters for creating a sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)
radius = 2

# Coordinates for the sphere
x = radius * np.sin(v) * np.cos(u)
y = radius * np.sin(v) * np.sin(u)
z = radius * np.cos(v)

# Plot the surface of the sphere
ax.plot_surface(x, y, z, color='r', alpha=0.5)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot 
plt.show()