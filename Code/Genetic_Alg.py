from ProblemFile import ProblemClass
import ExTSP_Problem
import random
global the_problem
from operator import attrgetter
class GeneticAlgorithm:
    population=4#TODO: increase it
    variance = 0.01
    max_iteration=2
    # parent = 20
    mutation_probability=0.4
    mean=0
    def __init__(self, problem : ProblemClass):
        global the_problem
        the_problem = problem
        self.my_problem=problem
        self.people = []
        self.best_fitness = []
        self.worst_fitness = []
        self.avrage_fitness = []
    def iterate (self):
        new_generation = []
        for i in range (0, self.population):
            X=self.find_parent()
            Y=self.find_parent()
            tmp_state=self.my_problem.reproduce(X.state, Y.state)
            if (random.uniform(0,1) < self.mutation_probability ):
                # tmp_state=self.my_problem.mutate(tmp_state)
                no_action_done=True
                #TODO: implement mutaion
            child= Node (tmp_state, self.my_problem.cost(tmp_state))
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
        print("Best chromosome: ")
        print(self.my_problem.return_state(best_node.state), " cost:", str(best_node.cost))
        # TODO: we did like code in Reference book
        self.people=self.select_for_next_generation(new_generation)

    def select_for_next_generation(self, new_generation):
        print ("next generation: ")
        new_people = []
        new_generation = sorted(new_generation, key=attrgetter('fitness'), reverse=True)
        self.people = sorted(self.people, key=attrgetter('fitness'), reverse=True)
        for i in range (0, int(len(new_generation)/2)):
            new_people.append(new_generation[i])
        for i in range (0, int(len(self.people)/2)):
            new_people.append(self.people[i])
        for i in new_people:
            print(self.my_problem.return_state(i.state), " cost:", str(i.cost))
        return new_people

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

    def make_initial_population(self):
        print("First population: ")
        for i in range (0, self.population):
            tmp_state=self.my_problem.get_initial_state_random()
            tmp_node=Node(tmp_state, self.my_problem.cost(tmp_state))
            self.people.append(tmp_node)
            self.my_problem.show_state(tmp_state)

    def initialization (self):
        self.people = []
        self.best_fitness = []
        self.worst_fitness = []
        self.avrage_fitness = []
        self.make_initial_population()

    def genetic_alg (self):
        self.initialization()
        for i in range (0, self.max_iteration):
            print("iteration ", i)
            self.iterate()
        print("result: ")
        best_node=max (self.people, key=attrgetter("fitness"))
        print(self.my_problem.return_state(best_node.state),  " cost:", str(best_node.cost) )

    def show_result(self):
        print("best in time: ")
        for i in range(0, self.max_iteration):
            print(self.best_fitness[i])
        print("worst in time: ")
        for i in range(0, self.max_iteration):
            print(self.worst_fitness[i])
        print("average in time: ")
        for i in range(0, self.max_iteration):
            print(self.avrage_fitness[i])

class Node:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost
        self.fitness = the_problem.fitness(self.cost)

problem_class = ProblemClass()
problem = ExTSP_Problem.ExTSP_Problem()
alg = GeneticAlgorithm(problem)
alg.genetic_alg()
alg.show_result()