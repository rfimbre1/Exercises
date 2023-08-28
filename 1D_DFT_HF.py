# 1 Dimensional DFT calculation using the Hartree-Fock method.

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
#

# Iterative self-consistent loop
for iter in range(50):
    # Calculate Hartree term
    rho = np.abs(psi)**2
    V_hartree = np.convolve(rho.sum(axis=1), np.roll(V_ext, L // 2), mode='same')
    
    # Check
    print(f"iter: {iter}")
    print("psi:", psi)
    print("rho:", rho)
    print("V_hartree:", V_hartree)
    #

    # Solution of the Kohn-sham equations using the Hartree potential
    for i in range(N):
        H_eff = -0.5 * np.gradient(np.gradient(psi[:, i])) + V_hartree * psi[:, i]
        psi[:, i] = np.linalg.eigvalsh(np.diag(H_eff))[i]
    
    # Normalize wavefunctions
    psi /= np.linalg.norm(psi, axis=0)

# Calculate total electron density
total_density = np.sum(np.abs(psi)**2, axis=1)

# Plotting
plt.plot(np.arange(L), total_density)
plt.xlabel('Lattice Site')
plt.ylabel('Electron Density')
plt.title('Simple DFT Calculation')
plt.show()

# Incomplete, code needs debugging. 
# Issue in: 'rho', 'psi' and 'V_hartree' evolution.