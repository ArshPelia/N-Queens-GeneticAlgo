# Arshjit Pelia 0374870
# Nikholas Pcenicni 0389088

import random
import time

# Defines global variables
POP_SIZE = 100 # number of chromosomes in the population
NUM_QUEENS = 8 # number of queens in the board
MAX_SOL = 92 # max number of solutions to find (Must be accurate for NUM_QUEENS)

# Generates a random chromosome
# A chromosome is a list of NUM_QUEENs integers, each index representing the column of the queen and the integer representing the row.
# The integers are between 0 and NUM_QUEENS-1 inclusive, with no repeated integers.
def generate_chromosome():
    chromosome = []
    used = []
    for i in range(NUM_QUEENS):
        while True:
            num = random.randint(0,NUM_QUEENS-1)
            if num not in used:
                chromosome.append(num)
                used.append(num)
                break
    return chromosome

# Calculates the fitness score of a chromosome
# The fitness score is the number of pairs of queens that are attacking each other.
# The goal is to find a chromosome with a fitness score of 0. (i.e. minimize the fitness score)
def fitness(chromosome):
    fitness = 0
    for i in range(NUM_QUEENS):
        for j in range(i+1,NUM_QUEENS):
            if chromosome[i] == chromosome[j]:
                fitness += 1
            if abs(chromosome[i] - chromosome[j]) == abs(i-j):
                fitness += 1
    return fitness

# Crosses over two chromosomes
# Crossover only occurs so that there are no repeated numbers in the chromosome (i.e. no two queens are in the same row).
# The crossover point is a random integer between 0 and NUM_QUEENS-1 inclusive.
def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(0,NUM_QUEENS-1)
    new_chromosome1 = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    new_chromosome2 = chromosome2[:crossover_point] + chromosome1[crossover_point:]
    used1 = []
    used2 = []
    for i in range(NUM_QUEENS):
        while new_chromosome1[i] in used1:
            new_chromosome1[i] = random.randint(0,NUM_QUEENS-1)
        used1.append(new_chromosome1[i])
        while new_chromosome2[i] in used2:
            new_chromosome2[i] = random.randint(0,NUM_QUEENS-1)
        used2.append(new_chromosome2[i])
    return new_chromosome1, new_chromosome2

# Mutation of a chromosome
# Akin to the crossover operator mutation only occurs so that there are no repeated numbers in the chromosome (i.e. no two queens are in the same row).
# The mutation point is a random integer between 0 and NUM_QUEENS-1 inclusive.
def mutation(chromosome):
    mutation_point = random.randint(0,NUM_QUEENS-1)
    new_chromosome = chromosome[:]
    new_chromosome[mutation_point] = random.randint(0,NUM_QUEENS-1)
    used = []
    for i in range(NUM_QUEENS):
        while new_chromosome[i] in used:
            new_chromosome[i] = random.randint(0,NUM_QUEENS-1)
        used.append(new_chromosome[i])
    return new_chromosome

# Prints the board of a chromosome
# The board is a NUM_QUEENSxNUM_QUEENS matrix of .s and Qs, where Q represents a queen.
def print_board(chromosome):
    print(chromosome)
    print()
    for i in range(NUM_QUEENS):
        for j in range(NUM_QUEENS):
            if chromosome[i] == j:
                print("Q", end = " ")
            else:
                print(".", end = " ")
        print()

# Finds the first solution found by the genetic algorithm
# The genetic algorithm will stop when a solution is found.
def find_first_solution():
    population = []
    for i in range(POP_SIZE):
        population.append(generate_chromosome())
    while True:
        new_population = []
        for i in range(POP_SIZE):
            chromosome1 = population[random.randint(0,POP_SIZE-1)]
            chromosome2 = population[random.randint(0,POP_SIZE-1)]
            new_chromosome1, new_chromosome2 = crossover(chromosome1, chromosome2)
            if fitness(new_chromosome1) < fitness(chromosome1):
                new_chromosome1 = mutation(new_chromosome1)
            if fitness(new_chromosome2) < fitness(chromosome2):
                new_chromosome2 = mutation(new_chromosome2)
            new_population.append(new_chromosome1)
            new_population.append(new_chromosome2)
        population = new_population
        for i in range(POP_SIZE):
            if fitness(population[i]) == 0:
                return population[i]

# Finds all solutions found by the genetic algorithm
# Mutation only occurs if fitness score is better than the previous one.
# The genetic algorithm will stop when MAX_SOL solutions are found.
def find_all_solutions():
    population = []
    for i in range(POP_SIZE):
        population.append(generate_chromosome())
    solutions = []
    while len(solutions) < MAX_SOL:
        new_population = []
        for i in range(POP_SIZE):
            chromosome1 = population[random.randint(0,POP_SIZE-1)]
            chromosome2 = population[random.randint(0,POP_SIZE-1)]
            new_chromosome1, new_chromosome2 = crossover(chromosome1, chromosome2)
            if fitness(new_chromosome1) < fitness(chromosome1):
                new_chromosome1 = mutation(new_chromosome1)
            if fitness(new_chromosome2) < fitness(chromosome2):
                new_chromosome2 = mutation(new_chromosome2)
            new_population.append(new_chromosome1)
            new_population.append(new_chromosome2)
        population = new_population
        for i in range(POP_SIZE):
            if fitness(population[i]) == 0 and population[i] not in solutions:
                solutions.append(population[i])
    return solutions

#main function
def main():
    start_time = time.time()
    print()
    print("First solution:", end=" ")
    first_solution = find_first_solution()
    print_board(first_solution)
    print()
    print("Time to find first solution: %s seconds" % (time.time() - start_time))
    print()
    start_time = time.time()
    all_solutions = find_all_solutions()
    print("Time to find all solutions: %s seconds" % (time.time() - start_time))
    print()
    response = input(f"Would you like to see all {len(all_solutions)} solutions? (y/n): ")
    if response == "y":
        print()
        print(f"All {len(all_solutions)} solutions:")
        for i in range(len(all_solutions)):
            print("Solution %s:" % (i+1), end = " ")
            print_board(all_solutions[i])
            print()
            if i % 10 == 0 and i != 0: 
                input("Press enter to view the next 10 solutions...")

    print("Program finished!")

main()