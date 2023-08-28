# This program calculates the time "t" of a falling  
# object (ignoring air resistance) at a given height "h".

import numpy as np
import time

print("This program calculates the time elapsed during the free fall at a given height.")
print("We assume the dropped objects falls with a magnitude of acceleration due to gravity of 9.81 m/s^2 and ignore the air resistance.")

h = input("Enter the height (m) at which the object is being dropped: ")
h = float(h)

v = input("Enter the initial velocity (m/s) at which the object is dropped: ")
v = float(v)

start = time.time()

print("The object was dropped from a height of", h, "meters. At a velocity of", v, "m/s.")

g = 9.81 
vf = np.sqrt(v**2 + 2*g*h)
t = (vf - v) / g

print("The time elapsed during the free fall is:", t, "seconds.")
print("It's final velocity was:", vf,"m/s.")

end = time.time()

print("Computation time:", end-start, "seconds.")
