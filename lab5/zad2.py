import pygad
import numpy as np
import math

# Funkcja, którą chcemy maksymalizować
def endurance(x, y, z, u, v, w):
    return math.exp(-2*(y - math.sin(x))**2) + math.sin(z*u) + math.cos(v*w)

# Funkcja fitness dla PyGAD
def fitness_func(model, solution, solution_idx):
    x, y, z, u, v, w = solution
    return endurance(x, y, z, u, v, w)

# gen to liczba z przedziału [0, 1]
gene_space = {'low': 0.0, 'high': 1.0}

# Parametry algorytmu
sol_per_pop = 20    
num_genes = 6
num_generations = 80
num_parents_mating = 10
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 25

ga_instance = pygad.GA(
    gene_space=gene_space,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    keep_parents=keep_parents,
    parent_selection_type=parent_selection_type,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes
)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : ", solution)
print("Fitness value of the best solution =", solution_fitness)

ga_instance.plot_fitness()
