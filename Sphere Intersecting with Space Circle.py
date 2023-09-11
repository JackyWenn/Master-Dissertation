import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D coordinate axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Sphere parameters
center_sphere = np.array([0.5, 0.5, 0.5])  # Center coordinates of the sphere
radius_sphere = 0.5  # Sphere radius

# Circle parameters
center_circle = np.array([0.4, 0.1, 0.4])  # Center coordinates of the circle, not coinciding with the sphere center
normal_vector = np.array([1, 1, 0])  # Normal vector of the plane containing the circle
radius_circle = 0.6  # Circle radius

# Calculate points of intersection between the sphere surface and the plane of the circle
v1 = center_circle - center_sphere
v1 /= np.linalg.norm(v1)

# Check if the normal vector is a zero vector
if np.linalg.norm(normal_vector) == 0:
    normal_vector = np.array([1, 0, 0])  # Handle a special case where the normal vector has zero length

# Calculate the angle between v1 and the normal vector
angle = np.arccos(np.dot(v1, normal_vector) / (np.linalg.norm(v1) * np.linalg.norm(normal_vector)))

# If v1 is parallel to the normal vector, choose a vector perpendicular to v1 as v2
if np.isclose(angle, 0) or np.isclose(angle, np.pi):
    v2 = np.array([0, 0, 1])
else:
    v2 = np.cross(normal_vector, v1)
    v2 /= np.linalg.norm(v2)

v3 = np.cross(v1, v2)
point_on_sphere = center_circle + radius_circle * np.cos(np.linspace(0, 2 * np.pi, 100))[:, None] * v2 + radius_circle * np.sin(np.linspace(0, 2 * np.pi, 100))[:, None] * v3

# Plot the surface of the sphere
u_sphere = np.linspace(0, 2 * np.pi, 100)
v_sphere = np.linspace(0, np.pi, 100)
u_sphere, v_sphere = np.meshgrid(u_sphere, v_sphere)
x_sphere = center_sphere[0] + radius_sphere * np.sin(v_sphere) * np.cos(u_sphere)
y_sphere = center_sphere[1] + radius_sphere * np.sin(v_sphere) * np.sin(u_sphere)
z_sphere = center_sphere[2] + radius_sphere * np.cos(v_sphere)
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='blue', alpha=0.3)

# Plot the intersecting circle
ax.plot(point_on_sphere[:, 0], point_on_sphere[:, 1], point_on_sphere[:, 2], color='orange', linewidth=2)

# Set plot attributes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sphere Intersecting with Space Circle')

# Show the plot
plt.show()