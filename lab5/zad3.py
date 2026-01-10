import pygad
import numpy as np

#macierz
lab = [
    [0,0,0,1,0,0,0,0,0,0],
    [1,1,0,1,0,1,1,1,1,0],
    [0,0,0,1,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,0,1,0],
    [0,1,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,0,1,0,1,0],
    [0,1,0,1,0,0,0,0,1,0],
    [0,1,0,1,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,0,0,0]
]

ROWS, COLS = 10, 10
START = (0, 0)
END = (9, 9)
MAX_STEPS = 30


# === FUNKCJA FITNESS ===
def fitness_func(model, solution, solution_idx):
    x, y = START

    for move in solution:
        if move == 0: x -= 1
        elif move == 1: x += 1
        elif move == 2: y -= 1
        elif move == 3: y += 1

        if x < 0 or x >= ROWS or y < 0 or y >= COLS:
            return 1
        if lab[x][y] == 1:
            return 1
        if (x, y) == END:
            return 1000

    dist = abs(x - END[0]) + abs(y - END[1])
    return 1000 - dist


# === PARAMETRY GA ===
gene_space = [0, 1, 2, 3]  # 4 możliwe ruchy

ga = pygad.GA(
    num_generations=400,
    sol_per_pop=100,
    num_parents_mating=20,
    fitness_func=fitness_func,
    num_genes=MAX_STEPS,
    gene_space=gene_space,
    parent_selection_type="sss",
    keep_parents=4,
    crossover_type="single_point",
    mutation_type="random",
    mutation_percent_genes=10,
    stop_criteria=["reach_1000"]
)

# === URUCHOMIENIE ===
ga.run()

# === WYNIKI ===
solution, fitness, idx = ga.best_solution()
print("Najlepsza ścieżka:", solution)
print("Fitness:", fitness)

ga.plot_fitness()
