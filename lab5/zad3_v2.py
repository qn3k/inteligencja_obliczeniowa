import pygad
import numpy as np
import time

# === LABIRYNT ===
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

gene_space = [0, 1, 2, 3]

# === TWORZENIE NOWEJ INSTANCJI GA ===
def create_ga():
    return pygad.GA(
    num_generations=200,
    sol_per_pop=60,
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

SUCCESS_TARGET = 10
successful_times = []
attempt = 0

while len(successful_times) < SUCCESS_TARGET:
    attempt += 1
    ga = create_ga()

    start = time.time()
    ga.run()
    end = time.time()

    solution, fitness, _ = ga.best_solution()

    if fitness == 1000:
        t = end - start
        successful_times.append(t)
        print(f"UDANA próba #{len(successful_times)}: znaleziono w {t:.4f} s (globalna próba {attempt})")
    else:
        print(f"Nieudana próba {attempt} – brak rozwiązania")

print("\n========== PODSUMOWANIE ==========")
print(f"Znaleziono 10 udanych prób po {attempt} całkowitych uruchomieniach.")

avg_time = sum(successful_times) / len(successful_times)
print(f"Średni czas udanych prób: {avg_time:.4f} s")
