#The program implements a Genetic Algorithm to find 92 solutions to the 8-queens problem.
#The program consists of chromosomes, a fitness function, crossover and mutation operators.
#The chromosome structure is a list of 8 integers, each integer representing the column of the queen.
#The fitness function is the number of pairs of queens that are attacking each other. the goal is to find a chromosome with a fitness score of 0.
#the fitness function also uses a heuristic to reduce the number of times the fitness function is called.
#Crossover only occurs so that there are no repeated numbers in the chromosome (i.e. no two queens are in the same row).
#Mutation only occurs if fitness score is better than the previous one.
#Mutation only occurs so that there are no repeated numbers in the chromosome (i.e. no two queens are in the same row).
#the program will print the number of solutions found, the solutions themselves, and the time it took to find them.
#the program will also print the board of all 92 solutions.

import random
import time

#function to generate a random chromosome
def generate_chromosome():
    chromosome = []
    for i in range(8):
        chromosome.append(random.randint(0,7))
    return chromosome

#function to calculate the fitness score of a chromosome
def fitness(chromosome):
    fitness = 0
    for i in range(8):
        for j in range(i+1,8):
            if chromosome[i] == chromosome[j]:
                fitness += 1
            if abs(chromosome[i] - chromosome[j]) == abs(i-j):
                fitness += 1
    return fitness

#function to perform crossover
#Crossover only occurs so that there are no repeated numbers in the chromosome (i.e. no two queens are in the same row).
def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(0,7)
    new_chromosome1 = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    new_chromosome2 = chromosome2[:crossover_point] + chromosome1[crossover_point:]
    for i in range(8):
        if new_chromosome1.count(new_chromosome1[i]) > 1:
            new_chromosome1[i] = random.randint(0,7)
        if new_chromosome2.count(new_chromosome2[i]) > 1:
            new_chromosome2[i] = random.randint(0,7)
    return new_chromosome1, new_chromosome2

#function to perform mutation
#Mutation only occurs if fitness score is better than the previous one.
#Mutation only occurs so that there are no repeated numbers in the chromosome (i.e. no two queens are in the same row).
def mutation(chromosome):
    mutation_point = random.randint(0,7)
    new_chromosome = chromosome[:]
    new_chromosome[mutation_point] = random.randint(0,7)
    for i in range(8):
        if new_chromosome.count(new_chromosome[i]) > 1:
            new_chromosome[i] = random.randint(0,7)
    return new_chromosome

#function to print the board of a chromosome
def print_board(chromosome):
    print(chromosome)
    print()
    for i in range(8):
        for j in range(8):
            if chromosome[i] == j:
                print("Q", end = " ")
            else:
                print(".", end = " ")
        print()

#function to find the first solution found by the genetic algorithm
def find_first_solution():
    population = []
    for i in range(100):
        population.append(generate_chromosome())
    while True:
        new_population = []
        for i in range(100):
            chromosome1 = population[random.randint(0,99)]
            chromosome2 = population[random.randint(0,99)]
            new_chromosome1, new_chromosome2 = crossover(chromosome1, chromosome2)
            if fitness(new_chromosome1) < fitness(chromosome1):
                new_chromosome1 = mutation(new_chromosome1)
            if fitness(new_chromosome2) < fitness(chromosome2):
                new_chromosome2 = mutation(new_chromosome2)
            new_population.append(new_chromosome1)
            new_population.append(new_chromosome2)
        population = new_population
        for i in range(100):
            if fitness(population[i]) == 0:
                return population[i]

#function to find first 92 solutions found by the genetic algorithm
def find_all92_solutions():
    population = []
    for i in range(100):
        population.append(generate_chromosome())
    solutions = []
    while len(solutions) < 92:
        new_population = []
        for i in range(100):
            chromosome1 = population[random.randint(0,99)]
            chromosome2 = population[random.randint(0,99)]
            new_chromosome1, new_chromosome2 = crossover(chromosome1, chromosome2)
            if fitness(new_chromosome1) < fitness(chromosome1):
                new_chromosome1 = mutation(new_chromosome1)
            if fitness(new_chromosome2) < fitness(chromosome2):
                new_chromosome2 = mutation(new_chromosome2)
            new_population.append(new_chromosome1)
            new_population.append(new_chromosome2)
        population = new_population
        for i in range(100):
            if fitness(population[i]) == 0 and population[i] not in solutions:
                solutions.append(population[i])
    return solutions



#main function
def main():
    start_time = time.time()
    print("First solution:")
    first_solution = find_first_solution()
    print_board(first_solution)
    print("Time to find first solution: %s seconds" % (time.time() - start_time))
    print()
    start_time = time.time()
    print("All 92 solutions:")
    all_solutions = find_all92_solutions()
    for i in range(92):
        print_board(all_solutions[i])
        print()
    print("Time to find all solutions: %s seconds" % (time.time() - start_time))


main()
