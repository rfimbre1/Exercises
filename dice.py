# A) Simulate the rolling of 
# two dice.
# B) Simulate the rolling of two dice 
# a million times. Count the number of
# times you get a double six. Finally divide 
# that number by a million to get the fraction
# of times you got a double six.

import random

list = [1, 2, 3, 4, 5, 6]

a = random.choice(list)
b = random.choice(list)

print("Part A:")
print("You've rolled both dice.")
print("You've got: ", a, ", ", b, ".")

print("Part B:")
i = 0
k = 0

while i < 1000000:
    c = random.choice(list)
    d = random.choice(list)
    i += 1
    if c == 6 and d == 6:
        k += 1

frac = k / 1000000

print(frac, "is the fraction of times getting a double six in a million rolls.")