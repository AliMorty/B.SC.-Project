import ProblemFile
import ExTSP_Problem
import math
from random import randint
import random
class Search:
    max_iteration = 1000
    def __init__(self, problem: ProblemFile.ProblemClass):
        self.my_problem=problem

        self.node_created=0
        self.node_expanded=0
        self.path = []
    def initial_before_start_search(self):
        self.node_created=0
        self.node_expanded=0
        self.path=[]
    def normal_hillclimbing (self):
        self.initial_before_start_search()
        tmp_state=self.my_problem.get_initial_state_random()
        current_node = Node(tmp_state, 0, self.my_problem.get_score(tmp_state), None)
        iteration_number=0
        best_node=None
        while (True):
            if self.my_problem.is_goal(current_node.state):
                self.show_result(current_node, True)
                return current_node
            if (iteration_number > self.max_iteration):
                break
            self.path.append(current_node)
            self.node_expanded += 1
            current_actions = self.my_problem.get_actions(current_node.state)

            best_node=Node (self.my_problem.get_result(current_node.state, current_actions[0]),
                            self.my_problem.get_cost(current_node.state,current_actions[0]),
                            self.my_problem.get_score(self.my_problem.get_result(current_node.state, current_actions[0])),
                            current_node )
            best_value = best_node.score
            for i in range (0, len(current_actions)):
                self.node_created +=1
                tmp_state=  self.my_problem.get_result(current_node.state, current_actions[i])
                # self.show_state(tmp_state)
                tmp_node = Node (tmp_state, self.my_problem.get_cost(current_node.state,current_actions[i]), self.my_problem.get_score(tmp_state), current_node )

                if self.my_problem.get_score(tmp_node.state) > best_value:
                    best_value = self.my_problem.get_score(tmp_node.state)
                    best_node = tmp_node


            if best_value > current_node.score:
                # print("YES THERE IS SOME INCREASE IN SCORE")
                current_node=best_node
            else:
                print("Here is a local maximum with value", current_node.score)
                self.show_result(current_node, True)
                return current_node

            iteration_number += 1
            print("iteration number", iteration_number)
    def stochastic_hillclimbing (self):
        self.initial_before_start_search()
        tmp_state = self.my_problem.get_initial_state_random()
        current_node = Node(tmp_state, 0, self.my_problem.get_score(tmp_state), None)
        iteration_number = 0
        best_node = None
        while (True):
            if self.my_problem.is_goal(current_node.state):
                self.show_result(current_node,True)
                return current_node
            if (iteration_number > self.max_iteration):
                break
            self.path.append(current_node)
            self.node_expanded += 1
            current_actions = self.my_problem.get_actions(current_node.state)
            useful_actions = []
            current_value = current_node.score
            for i in range(0, len(current_actions)):
                self.node_created += 1
                if (self.my_problem.get_score(self.my_problem.get_result(current_node.state, current_actions[i])) > current_value):
                    useful_actions.append(current_actions[i])
            if len(useful_actions)==0:
                print("Here is a local maximum with value", current_node.score)
                self.show_result(current_node, True)
                return current_node
            else:
                rand = randint(0, len(useful_actions)-1)
                tmp_state= self.my_problem.get_result(current_node.state, useful_actions[rand])
                current_node = Node(tmp_state, self.my_problem.get_cost(current_node, useful_actions[rand]), self.my_problem.get_score(tmp_state), current_node)
            iteration_number += 1
            print("iteration number", iteration_number)
    def best_first_hillclimbing (self):
        self.initial_before_start_search()
        tmp_state=self.my_problem.get_initial_state_random()
        current_node = Node(tmp_state, 0, self.my_problem.get_score(tmp_state), None)
        iteration_number=0
        best_node=None
        while (True):
            if self.my_problem.is_goal(current_node.state):
                self.show_result(current_node, True)
                return current_node
            if (iteration_number > self.max_iteration):
                break
            self.path.append(current_node)
            self.node_expanded += 1
            current_actions = self.my_problem.get_actions(current_node.state)


            for i in range (0, len(current_actions)):
                better_node_found=False
                self.node_created +=1
                tmp_state=  self.my_problem.get_result(current_node.state, current_actions[i])
                # self.show_state(tmp_state)
                tmp_node = Node (tmp_state, self.my_problem.get_cost(current_node.state,current_actions[i]), self.my_problem.get_score(tmp_state), current_node )
                if self.my_problem.get_score(tmp_node.state) > current_node.score:
                    current_node= tmp_node
                    better_node_found=True
                    break

            if better_node_found==False:
                print("Here is a local maximum with value", current_node.score)
                self.show_result(current_node, True)
                return current_node

            iteration_number += 1
            print("iteration number", iteration_number)
    def random_start_hillclimbing(self, necessary_score):
        self.initial_before_start_search()
        counter=1
        print("start search (" , counter, ")")
        test_node = self.normal_hillclimbing()
        print("end search (", counter, ") with score :", test_node.score)
        while (test_node.score < necessary_score):
            counter+=1
            print("start search (", counter, ")")
            test_node = self.normal_hillclimbing()
            print("end search (", counter, ") with score :" , test_node.score)
        print("We found it!")
        # self.show_state(test_node.state)

    def show_result(self, node, add_last):
        if (add_last):
            self.path.append(node)

        # self.my_problem.show_state(node.state)
        print("path: ")
        for i in range (0, len(self.path)):
            print("iteration", i, ":  score:", self.my_problem.get_score(self.path[i].state), " ", end='')
            self.my_problem.show_state(self.path[i].state)
        # print ("node score:", node.score)
        print("number of created nodes", self.node_created)
        print("number of expanded nodes", self.node_expanded)

    def show_state(self, state):
        print("state: ------------")
        self.my_problem.show_state(state)

    def schedule (self, t, schedule_number):
        T0=1000
        if (schedule_number==1): #normal schedule: linear
            return (T0 - t)/200
        if (schedule_number==2): #f(x)=1/(1+x)
            return T0/((1+t)*20)
        if (schedule_number==3): #f(x)= T0*(0.8^t)
            return T0*((0.8)**t)



    def simulated_annealing(self, schedule_number):
        self.initial_before_start_search()
        tmp_state = self.my_problem.get_initial_state_random()
        current_node = Node(tmp_state, 0, self.my_problem.get_score(tmp_state), None)
        self.path.append(current_node)
        t = 0
        best_node = None
        while (t<self.max_iteration):
            temperature = self.schedule(t, schedule_number)
            if (temperature ==0):
                print ("temp is 0 and result is ")
                self.show_result(current_node,True)
                return current_node
            if (self.my_problem.is_goal(current_node.state)==True):
                print("we found the goal")
                self.show_result(current_node,False)
                return current_node
            current_actions = self.my_problem.get_actions(current_node.state)
            rand = randint(0, len(current_actions) - 1)
            result_state = self.my_problem.get_result(current_node.state, current_actions[rand])
            tmp_node = Node (result_state, self.my_problem.get_cost(current_node.state, current_actions[rand]),
                                     self.my_problem.get_score(result_state), current_node)
            self.node_created += 1
            self.my_problem.show_state(tmp_node.state)
            if tmp_node.score >= current_node.score:
                current_node = tmp_node
                self.path.append(current_node)
                self.node_expanded += 1
            else:
                r = random.uniform(0, 1)
                delta_e = tmp_node.score - current_node.score
                probability = math.exp(delta_e/temperature)
                # probability = temperature**delta_e
                print("probability: ", probability)
                if r < probability:
                    current_node = tmp_node
                    self.path.append(current_node)
                    self.node_expanded += 1
            t += 1

        print("max iteration exceeded and result is:")
        self.show_result(current_node, True)
        return current_node


class Node :
    def __init__(self, state, cost, score, parent):
        self.state=state
        self.current_cost=cost
        self.score=score
        self.parent=parent
        if (parent==None):
            self.total_cost=self.current_cost
        else:
            self.total_cost=parent.current_cost+self.current_cost

Problem = ExTSP_Problem.ExTSP_Problem()

ProblemSolverAgent = Search(Problem)
# ProblemSolverAgent.simulated_annealing(1)
# ProblemSolverAgent.simulated_annealing(2)
ProblemSolverAgent.simulated_annealing(3)



# ProblemSolverAgent.normal_hillclimbing()
# ProblemSolverAgent.stochastic_hillclimbing()
# ProblemSolverAgent.best_first_hillclimbing()
# ProblemSolverAgent.random_start_hillclimbing(0)




# print (math.exp(-2/(0.99**500)))