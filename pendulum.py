# Visual simulation of a pendulum.

import numpy as np 
import matplotlib.pyplot as plt
import scipy
from scipy.special import ellipk
import matplotlib.animation as animation

# We establish the physical properties of the pendulum.
# Mass 'm' (kg), pendulum's length 'L' (m), acceleration due to gravity 'g' (m/s^2)

m, L, g = 1, 1, 9.81

# We set: initial angular displacement 'th0' (rad), tangential velocity 'v0' (m/s)

th0, v0 = np.radians(60), 0

# We estimate the pendulum's period using a harmonic small displacement approximation.

T_harm = 2 * np.pi * np.sqrt(L/g)

# We now set a time step 'dt' (s) to be used in the integration of the equation of motion.

dt = 0.001

# We set: initial angular position and tangential velocity.

th, v = [th0], [v0]
o_th = th0
i = 0
while True:
    # We use a forward Euler method for the integration of the ODE.
    i += 1
    t = i * dt
    # We update the mass's position by using the updated angle.
    o_th, o_v = th[-1], v[-1]
    omega = o_v / L
    n_th = o_th - (omega * dt)

    # Tangential acceleration.
    acc = g * np.sin(o_th)
    # Tangential velocity update.
    n_v = o_v + (acc * dt)

    if t > T_harm and n_v * o_v < 0:
        # Meaning this is a second turning and completing one period.
        break
    th.append(n_th)
    v.append(n_v)

# We calculate the estimated pendulum's period, T, from the integration,
# and the "exact" value in terms of the complete integral of the first kind.

nsteps = len(th)
T = nsteps * dt
print('Calculated period, T = {} s'.format(T))
print('Estimated small-displacement angle period, T_harm = {} s'.format(T_harm))
k = np.sin(th0/2)
print('SciPy calculated period, T = {} s'.format(2 * T_harm / np.pi * ellipk(k**2)))

def get_coords(theta):
    """Return the (x, y) coordinates of the mass at angle theta."""
    return L * np.sin(th), -L * np.cos(theta)

# We initiate the animation plot. We set the aspect ratio equal for it to look right.
fig = plt.figure()
ax = fig.add_subplot(aspect='equal')
# The pendulum rod, in its initial position.
x0, y0 = get_coords(th0)
line, = ax.plot([0, x0], [0, y0], lw=3, c='k')
# The mass: we set zorder so that it is drawn over the pendulum rod.
mass_radius = 0.08
circle = ax.add_patch(plt.Circle(get_coords(th0), mass_radius, fc='r', zorder=3))
# Set plot limits for the pendulum to swing.
ax.set_xlim(-L*1.2, L*1.2)
ax.set_ylim(-L*1.2, L*1.2)

def animate(i):
    """Update the animation at frame i."""
    x, y = get_coords(th[i])
    line.set_data([0, x], [0, y])
    circle.set_center((x, y))

nframes = nsteps
interval = dt * 1000
ani = animation.FuncAnimation(fig, animate, frames=nframes, repeat=True, interval=interval)

plt.show()

# Incomplete needs debugging.