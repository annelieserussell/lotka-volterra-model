# 05/08/25 Lotka-Volterra Predator-Prey Model
# Author: AR
# Description: Simulates predator-prey dynamics using the Lotka-Volterra equations.
# The model allows for user-defined parameters, initial conditions, and time range.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Ask user for parameters
alpha = float(input("Enter alpha (prey growth rate): "))
beta = float(input("Enter beta (predation rate): "))
delta = float(input("Enter delta (predator reproduction rate): "))
gamma = float(input("Enter gamma (predator death rate): "))

# Ask user for initial conditions
x0 = float(input("Enter initial prey population: "))
y0 = float(input("Enter initial predator population: "))
X0 = [x0, y0]

# Ask user for time range
t_max = float(input("Enter simulation time (e.g., 100): "))
t_points = int(input("Enter number of time points (e.g., 1000): "))
t = np.linspace(0, t_max, t_points)

# Lotka-Volterra function
def lotka_volterra(X, t, alpha, beta, delta, gamma):
    x, y = X # Unpack prey (x) and predator (y) populations

    # Rate of change of prey
    dxdt = alpha * x - beta * x * y # Prey growth rate - Predation rate

    # Rate of change of predators
    dydt = delta * x * y - gamma * y # Predator reproduction rate - Predator death rate

    return [dxdt, dydt]

# Solve system
solution = odeint(lotka_volterra, X0, t, args=(alpha, beta, delta, gamma))
x, y = solution.T

# Plot the results
plt.plot(t, x, label="Prey")
plt.plot(t, y, label="Predators")
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model: Prey and Predator Populations')
plt.legend()
plt.grid(True)
plt.show()
