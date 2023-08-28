# 1-Dimensional Ising Model

import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 50 # Number of spins
J = 1 # Interaction strength
T = np.linspace(0.1, 5, 20) # Temperatures

# Random spin config.
spins = np.random.choice([-1, 1], size=L)

# Metropolis algorithm for spin updates.
def metro(spin, nexto, beta):
    en_diff = 2 * J * spin * np.sum(nexto)
    if en_diff < 0 or np.random.rand() < np.exp(-beta * en_diff):
        return -spin
    return spin

# Simulation
magnets = []

for temp in T:
    beta = 1 / temp
    magnet = np.mean(spins)
    for _ in range(1000): # Equilibration
        rand_idx = np.random.randint(L)
        nexto = spins[(rand_idx - 1) % L] + spins[(rand_idx + 1) % L]
        spins[rand_idx] = metro(spins[rand_idx], nexto, beta)
    magnet = []
    for _ in range(10000): # Data collection
        rand_idx = np.random.randint(L)
        nexto = spins[(rand_idx - 1) % L] + spins[(rand_idx + 1) % L]
        spins[rand_idx] = metro(spins[rand_idx], nexto, beta)
        magnet.append(np.mean(spins))
    magnets.append(np.mean(magnet))

# Plotting
plt.plot(T, np.abs(magnets), color='violet', marker='o')
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.title('Ising Model Simulation (1D)')
plt.show()