import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 100 # Number of lattice sites
N = 50 # Number of electrons
V_ext = np.cos(2 * np.pi * np.arange(L) / L) # External potential

# Initialize wavefunctions
psi = np.random.rand(L, N) + 1j * np.random.rand(L, N)
psi /= np.linalg.norm(psi, axis=0) # Normalize

# Check
print("psi1:", psi)