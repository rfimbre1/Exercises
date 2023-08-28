# Use of a Monte Carlo simulation to estimate the value of pi.

import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_points = 10000 # Number of random points to generate
points = np.random.rand(n_points, 2) # Generation of random points in the [0, 1) x [0, 1) square
dist = np.linalg.norm(points, axis=1) # Calculation for the distances for each point from the origin
p_ins_circle = np.sum(dist <= 1) # Count num. of points inside circle (<= 1)
est_pi = 4 * (p_ins_circle / n_points) # Estimate pi as the ratio of points inside the circle to total points

print("Estimated π: ", est_pi)

# Visualization
plt.figure(figsize=(6, 6))
plt.scatter(points[:, 0], points[:, 1], color='orange', s=1)
plt.title(f"Monte Carlo Estimation of π: {est_pi:.6f}")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().add_artist(plt.Circle((0, 0), 1, color='red', alpha=0.3))
plt.show()
