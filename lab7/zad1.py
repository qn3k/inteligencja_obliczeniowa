import numpy as np
import math
import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history



# Funkcja endurance 
def endurance(x):
    # x = [x, y, z, u, v, w]
    return (
        math.exp(-2 * (x[1] - math.sin(x[0]))**2)
        + math.sin(x[2] * x[3])
        + math.cos(x[4] * x[5])
    )



def objective_function(X):
    n_particles = X.shape[0]
    costs = np.zeros(n_particles)

    for i in range(n_particles):
        costs[i] = -endurance(X[i])  # minus = maksymalizacja

    return costs


# Ograniczenia dziedziny
x_min = np.zeros(6)
x_max = np.ones(6)
bounds = (x_min, x_max)


# Parametry PSO
options = {
    'c1': 0.5,   # składnik poznawczy
    'c2': 0.3,   # składnik społeczny
    'w': 0.9     # bezwładność
}


# Inicjalizacja optymalizatora
optimizer = ps.single.GlobalBestPSO(
    n_particles=30,
    dimensions=6,
    options=options,
    bounds=bounds
)


# Uruchomienie optymalizacji
best_cost, best_pos = optimizer.optimize(
    objective_function,
    iters=200
)


# Wyniki
print("Najlepszy koszt (z minusem):", best_cost)
print("Najlepsza pozycja:", best_pos)
print("Maksymalna endurance:", -best_cost)


# Wykres historii kosztu
plot_cost_history(optimizer.cost_history)
plt.title("PSO - historia kosztu (stop metali)")
plt.xlabel("Iteracja")
plt.ylabel("Koszt")
plt.show()
