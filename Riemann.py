import numpy as np

print("This program solves a Riemann integral of integrand:")
print("sqrt(1 - x^2)")

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("The given value is not an INTEGER. Try again.")
            continue
        else:
            return userInput
            break

N = inputNumber("Enter the N amount of slices to compute the integral: N = ")

h = 2/N
k = 1
InteF = 0

for i in range(k, N):
    xk = -1 + h*k
    yk = np.sqrt(1 - xk**2)
    InteF = InteF + h * yk
    k += 1
    

print("The result of the Riemann integral is: ", InteF)
    
