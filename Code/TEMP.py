import pulp
import pandas as pd
import random
import numpy as np
import itertools
import copy
from deap import base
from deap import creator
from deap import tools




class genetic:

    global cost1_arr
    global cost2_arr
    global node_no
    global population_size

    def __init__(self):
        self.population_size = 100
        self.read_from_file()


    def reproduce(self, X, Y):
        a=2
    #     TODO:
    def iterate(self):
        new_generation = []
        for i in range (0, self.population_size):
            X=self.find_parent()
            Y=self.find_parent()
            tmp_state=self.reproduce(X, Y)
            if (random.uniform(0,1) < self.mutation_probability ):
                tmp_state=self.my_problem.mutate(tmp_state, self.mean, self.variance)
            child= Node (tmp_state, self.my_problem.fitness(tmp_state))
            new_generation.append(child)
        best_node=new_generation[0]
        best_fitness=new_generation[0].fitness
        worst_fitness=new_generation[0].fitness
        sum_fitness=0.0
        for i in range (0, self.population):
            tmp_val=new_generation[i].fitness
            if (tmp_val > best_fitness):
                best_node=new_generation[i]
                best_fitness=tmp_val
            if (tmp_val < worst_fitness):
                worst_fitness=tmp_val
            sum_fitness += tmp_val
        average_fitness = sum_fitness / self.population

        self.best_fitness.append(best_fitness)
        self.worst_fitness.append(worst_fitness)
        self.avrage_fitness.append(average_fitness)
        print("this round:")
        print("Best fitness:")
        self.my_problem.show_state(best_node.state)
        # TODO: we did like code in Reference book
        self.people=self.select_for_next_generation(new_generation)

    def find_parent(self):
        sum_fitness=0.0
        for i in range (0, self.population):
            sum_fitness += self.people[i].fitness
        rand_value = random.uniform(0, sum_fitness)
        for i in range (0, self.population):
            rand_value -= self.people[i].fitness
            if (rand_value <= 0):
                return self.people[i]
        print("problem in finding parent")
        return None




    def generate_initial_population(self, people_no):
        population = []
        for i in range(0, people_no):
            person = self.random_chromosome()
            population.append(person)
        return population
    def select_chromosome (self):
    #     TODO:
        a=2

    def evaluation(self, chromosome):
        return chromosome.get_cost()

    def evaluate_chromosome(self, chromosome):
        arr = copy.copy(cost1_arr)
        size = len(chromosome.path)
        cost = 0.0
        for i in range(0, size):
            j = i + 1
            if j == size:
                j = 0
            a=chromosome.path[i]
            b=chromosome.path[j]
            cost += arr[(a, b)]
            arr[(a, b)] = cost2_arr[(a, b)]
            arr[(a, b)] = cost2_arr[(a, b)]
        return cost

    class chromosome:
        path = []
        size = -1
        arr = None
        cost_calculated = False
        calculated_cost = - 1.0
        def __init__(self, list):
            self.path = list
            self.size = len(self.path)
            self.get_cost()
        def show_path(self):
            for i in self.path:
                print(i, end='')
            print ()
        def calculate_fitness(self):#it is only for DEAP library
            self.arr = copy.copy(cost1_arr)
            self.size = len(self.path)
            cost = 0.0
            for i in range(0, self.size):
                j = i + 1
                if j == self.size:
                    j = 0
                cost += arr[(i, j)]
                arr[(i, j)] = cost2_arr[(i, j)]
                arr[(j, i)] = cost2_arr[(i, j)]
            return cost
        def get_cost(self):
            if not self.cost_calculated:
                self.arr = copy.copy(cost1_arr)
                cost = 0.0
                for i in range (0, self.size):
                    j = i + 1
                    if j == self.size:
                        j=0
                    cost += arr[(i,j)]
                    arr[(i,j)]=cost2_arr[(i,j)]
                    arr[(j,i)]=cost2_arr[(i,j)]
                self.calculated_cost=cost
                self.cost_calculated=True
            return self.calculated_cost





# random_TSP_path(3)
GA = genetic()
arr = copy.copy(GA.cost1_arr)



