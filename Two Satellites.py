import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D coordinate axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters for Sphere 1
center1 = np.array([0, 0, 0])  # Coordinates of the sphere center
radius1 = 1.0  # Sphere radius

# Parameters for Sphere 2
center2 = np.array([0.5, 0.5, 0.5])  # Coordinates of the sphere center
radius2 = 0.8  # Sphere radius

# Calculate the coordinates of the intersection circle's center
intersection_center = (center1 + center2) / 2

# Calculate the radius of the intersection circle
intersection_radius = np.abs(radius1 - radius2) * 2.5  # Increase the intersection circle's radius

# Generate parameters for Sphere 1
u1 = np.linspace(0, 2 * np.pi, 100)
v1 = np.linspace(0, np.pi, 100)
u1, v1 = np.meshgrid(u1, v1)
x1 = center1[0] + radius1 * np.sin(v1) * np.cos(u1)
y1 = center1[1] + radius1 * np.sin(v1) * np.sin(u1)
z1 = center1[2] + radius1 * np.cos(v1)

# Plot the surface of Sphere 1 in blue with transparency
ax.plot_surface(x1, y1, z1, color='blue', alpha=0.3)

# Generate parameters for Sphere 2
u2 = np.linspace(0, 2 * np.pi, 100)
v2 = np.linspace(0, np.pi, 100)
u2, v2 = np.meshgrid(u2, v2)
x2 = center2[0] + radius2 * np.sin(v2) * np.cos(u2)
y2 = center2[1] + radius2 * np.sin(v2) * np.sin(u2)
z2 = center2[2] + radius2 * np.cos(v2)

# Plot the surface of Sphere 2 in red with transparency
ax.plot_surface(x2, y2, z2, color='red', alpha=0.3)

# Calculate parameters for the intersection circle
theta_intersect = np.linspace(0, 2 * np.pi, 100)
x_intersect = intersection_center[0] + intersection_radius * np.cos(theta_intersect)
y_intersect = intersection_center[1] + intersection_radius * np.sin(theta_intersect)
z_intersect = intersection_center[2] * np.ones_like(theta_intersect)

# Plot the contour of the intersection circle in orange
ax.plot(y_intersect, z_intersect, x_intersect, color='orange', linewidth=2)

# Set plot attributes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Intersecting Spheres with Intersection Circle')

# Show the plot
plt.show()