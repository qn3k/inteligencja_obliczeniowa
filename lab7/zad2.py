import matplotlib.pyplot as plt
import random
import math

from aco import AntColony

plt.style.use("dark_background")


# 15 LOSOWYCH PUNKTÓW Z PRZEDZIAŁU [0, 100]

def generate_random_coords(n=15, low=0, high=100):
    return tuple(
        (random.randint(low, high), random.randint(low, high))
        for _ in range(n)
    )


COORDS = generate_random_coords(15)


# Funkcje pomocnicze do rysowania
def plot_nodes(coords, w=12, h=8):
    for x, y in coords:
        plt.plot(x, y, "g.", markersize=12)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_path(path):
    for i in range(len(path) - 1):
        plt.plot(
            (path[i][0], path[i + 1][0]),
            (path[i][1], path[i + 1][1]),
            "r-"
        )


def path_length(path):
    length = 0.0
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        length += math.dist((x1, y1), (x2, y2))
    return length


# c) EKSPERYMENTY 
experiments = [
    {"ant_count": 50, "alpha": 0.5, "beta": 1.2, "evap": 0.4},
    {"ant_count": 100, "alpha": 1.0, "beta": 2.0, "evap": 0.3},
    {"ant_count": 200, "alpha": 1.5, "beta": 3.0, "evap": 0.2},
]

best_overall = None
best_length = float("inf")

for i, params in enumerate(experiments):
    colony = AntColony(
        COORDS,
        ant_count=params["ant_count"],
        alpha=params["alpha"],
        beta=params["beta"],
        pheromone_evaporation_rate=params["evap"],
        pheromone_constant=1000.0,
        iterations=300
    )

    path = colony.get_path()
    length = path_length(path)

    print(f"Eksperyment {i+1}: długość trasy = {length:.2f}")

    if length < best_length:
        best_length = length
        best_overall = path


# Rysowanie
plot_nodes(COORDS)
plot_path(best_overall)
plt.title(f"Najlepsza trasa (długość = {best_length:.2f})")
plt.show()


#grid

GRID_COORDS = tuple(
    (x, y)
    for y in range(0, 50, 10)
    for x in range(0, 50, 10)
)

colony_grid = AntColony(
    GRID_COORDS,
    ant_count=300,
    alpha=1.0,
    beta=2.0,
    pheromone_evaporation_rate=0.3,
    pheromone_constant=1000.0,
    iterations=400
)

grid_path = colony_grid.get_path()
grid_length = path_length(grid_path)

plot_nodes(GRID_COORDS, w=10, h=10)
plot_path(grid_path)
plt.title(f"Grid 5x5 – długość trasy = {grid_length:.2f}")
plt.show()

print("Długość trasy dla gridu 5x5:", grid_length)
