import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class MechanicalSystem:
    def __init__(self, m, k, c, F0, omega, x0, v0):
        self.m = m
        self.k = k
        self.c = c
        self.F0 = F0
        self.omega = omega
        self.y0 = [x0, v0]

    def model(self, y, t):
        x, v = y
        dxdt = v
        dvdt = (self.F0*np.cos(self.omega*t) - self.c*v - self.k*x) / self.m
        return [dxdt, dvdt]

    def solve(self, t):
        return odeint(self.model, self.y0, t)

# Paramètres
m = 10  # kg
k = 4000  # N/m
c = 20  # Ns/m
F0 = 100  # N
omega = 10  # rad/s
x0 = 0.01  # m
v0 = 0  # m/s

# Créer le système mécanique
system = MechanicalSystem(m, k, c, F0, omega, x0, v0)

# Temps
t = np.linspace(0, 10, 1000)

# Résoudre l'équation différentielle
y = system.solve(t)

# Plotter la réponse
plt.figure(figsize=(12, 6))
plt.plot(t, y[:, 0])
plt.title('Réponse du système')
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.grid(True)
plt.show()

# Calculer et plotter les énergies
Ec = 0.5 * m * y[:, 1]**2
Ep = 0.5 * k * y[:, 0]**2
Em = Ec + Ep

plt.figure(figsize=(12, 6))
plt.plot(t, Ec, label='Énergie cinétique')
plt.plot(t, Ep, label='Énergie potentielle')
plt.plot(t, Em, label='Énergie mécanique')
plt.title('Énergies du système')
plt.xlabel('Temps (s)')
plt.ylabel('Énergie (J)')
plt.legend()
plt.grid(True)
plt.show()
