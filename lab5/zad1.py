import pygad
import numpy as np

values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]  # wartość każdego przedmiotu
weights = [7, 7, 6 , 2, 5, 6, 1, 3, 10, 3 ,15]   # waga każdego przedmiotu
max_weight = 25                  # pojemność plecaka

gene_space = [0, 1]  

# Funkcja fitness
def fitness_func(model, solution, solution_idx):
    total_value = np.sum(solution * values)
    total_weight = np.sum(solution * weights)
    
    if total_weight > max_weight:
        return 0
    else:
        return total_value

fitness_function = fitness_func

# Parametry algorytmu
sol_per_pop = 20
num_genes = len(values)
num_parents_mating = 5
num_generations = 50
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10

# Inicjalizacja ga
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

# Uruchomienie algorytmu
ga_instance.run()

# Najlepsze rozwiązanie
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Najlepsze wybrane przedmioty: {solution}".format(solution=solution))
print("Łączna wartość: {solution_fitness}".format(solution_fitness=solution_fitness))
total_weight = np.sum(solution * weights)
print("Łączna waga: {total_weight}".format(total_weight=total_weight))

# Wykres ewolucji fitness
ga_instance.plot_fitness()
