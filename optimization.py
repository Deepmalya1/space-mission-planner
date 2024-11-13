import random
def genetic_algorithm_optimization(population_size,generations):
    population = [random.uniform(0,1) for _ in range(population_size)]
    for _ in range(generations):
        population=sorted(population)
        population = population[:population_size//2]+[random.uniform(0,1) for _ in range(population_size//2)]

    return population[0]
# print(genetic_algorithm_optimization(100, 2))