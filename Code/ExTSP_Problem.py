from ProblemFile import ProblemClass
import pulp
import pandas as pd
import random
import mst
import numpy as np
from mst import MinSpanTreeClass
import copy

import random
import math

class ExTSP_Problem(ProblemClass):
    global cost1_arr
    global cost2_arr

    global population_size
    global MST_class

    MST_class = MinSpanTreeClass()
    def __init__(self):
        self.read_from_file()
        self.infinity = 99999999.99
        self.frequency = None
        self.node_no = -1
        self.read_from_file()
    def read_from_file(self):
        cost1_df = pd.DataFrame.from_csv('./maps/1/cost1.csv', header=None, index_col=None)
        cost2_df = pd.DataFrame.from_csv('./maps/1/cost2.csv', header=None, index_col=None)
        global cost1_arr
        global cost2_arr
        cost1_arr = cost1_df.as_matrix(columns=None)
        cost2_arr = cost2_df.as_matrix(columns=None)

        self.cost1_arr = cost1_arr
        self.cost2_arr = cost2_arr


        self.node_no = len(cost1_arr)
    def random_path(self):
        check_list = list(range(1, self.node_no))
        remaining = len(check_list)
        output = []
        output.append(0)
        for i in range(0, remaining):
            r = random.randint(0, remaining - 1)
            app = check_list[r]
            del check_list[r]
            output.append(app)
            remaining -= 1
        return output
    def get_initial_state_random(self):
        state = self.random_path()
        return state
    def mutate (self, state):
        new_state = state[:]#TODO: Implement the Mutation
        return new_state
    def reproduce(self, state1, state2):

        inf = self.infinity
        arr_size = len(cost1_arr)

        arr = np.full ((arr_size, arr_size), self.infinity, dtype=float)
        n = len(state1)
        for i in range (0, n):
            j = i + 1
            if j == n:
                j=0
            a = state1[i]
            b = state1[j]
            arr[(a, b)] = cost1_arr[(a,b)]
            arr [(b,a)] = cost1_arr[(a,b)]
        n = len(state2)
        for i in range(0, n):
            j = i + 1
            if j == n:
                j = 0
            a = state2[i]
            b = state2[j]
            arr[(a, b)] = cost1_arr[(a, b)]
            arr[(b, a)] = cost1_arr[(a, b)]
        #arr is ready
        #calculate MST and make path from MST:
        global MST_class
        path = MST_class.do_all(arr)
        return path
    def show_state(self, state):
        n = len(state)
        print ("state =", end='')
        for i in range (n):
            print (state[i], end='')
        print()
    def return_state(self, state):
        string ="["
        n = len(state)
        for i in range(n):
            string += str(state[i])
            string +=", "
        string += "]"
        return string
    def get_path_cost (self, path):
        arr = copy.copy(cost1_arr)
        size = len(path)
        cost = 0.0
        for i in range(0, size):
            j = i + 1
            if j == size:
                j = 0
            a = path[i]
            b = path[j]
            cost += arr[(a, b)]
            arr[(a, b)] = cost2_arr[(a, b)]
            arr[(b, a)] = cost2_arr[(a, b)]
        return cost

        # if (chromosome.cost_calculated):
        #     return chromosome.cost
        # arr = copy.copy(cost1_arr)
        # size = len(chromosome.path)
        # cost = 0.0
        # for i in range(0, size):
        #     j = i + 1
        #     if j == size:
        #         j = 0
        #     a = chromosome.path[i]
        #     b = chromosome.path[j]
        #     cost += arr[(a, b)]
        #     arr[(a, b)] = cost2_arr[(a, b)]
        #     arr[(b, a)] = cost2_arr[(a, b)]
        # chromosome.set_cost(cost)
        # return cost
    def fitness (self, cost):
        return 1 / cost
    def cost (self, state):
        cost = self.get_path_cost(state)
        return cost
    # def show_state(self, state):
    #     print( state.path_to_string() + "  fitness:", self.fitness(state))


# class state:
#     def __init__(self, list):
#         self.cost_calculated = False
#         self.cost = -1
#         self.state = list
#         self.size = len(self.state)
#
#     def set_cost (self, cost):
#         self.cost_calculated=True
#         self.cost = cost
#         self.state = []
#
#     def show_path(self):
#         for i in self.state:
#             print(i, end='')
#         print()
#
#     def path_to_string(self):
#         string = "["
#         for i in self.state:
#             string = string + str(self.state[i]) + ", "
#         string += "]"
#         return string

    def get_cost(self, state, action):
        return 1
    def get_score(self, state):
        return -1 * self.get_path_cost(state)
    def is_goal(self, state):
        return False #this problem is optimization, and we cannot determine the asnwer
    def update_frequency (self, state):
        self.frequency = [0] * self.node_no
        for i in state:
            # print ("frequency: ", i)
            self.frequency[i] += 1
    def get_actions(self, state):
        self.update_frequency(state)
        tmp_cost_arr = self.modified_cost_array(state)

        #we should choose between increase and decrease path length:
        n = len(state)
        constant = 3


        tmp_val = min(n, constant* self.node_no )

        prob = float(1 - float((tmp_val - self.node_no)/(2*self.node_no)))
        r = random.uniform(0, 1)
        if (r < prob):
            # if we want to increase length:
            cost = []

            for i in range(0, n):
                j = i + 1
                if j == n:
                    j = 0
                a = state[i]
                b = state[j]
                c = tmp_cost_arr[(a, b)]
                new_val = self.cost_index(c, i)
                cost.append(new_val)
            selected_edge = self.select_roulete(cost)
            i = selected_edge.index
            j = i + 1
            if j == n:
                j = 0
            a = state[i]
            b = state[j]
            cost1 = tmp_cost_arr[(a, b)]
            cost2 = 0
            output = []
            index = i
            for new_n in range(0, self.node_no):
                if new_n == a or new_n == b:
                    continue
                cost2 = tmp_cost_arr[(a, new_n)] + tmp_cost_arr[(new_n, b)]
                # if (tmp_cost_arr[(a, new_n)] < cost1 or
                #             tmp_cost_arr[(new_n, b)] < cost1):
                output.append(self.ExTSP_action(index,"add",new_n))
            if len(output) == 0:
                print ("too bad")
            return output
        else:
            # if we want to decrease length:
            possible_remove_location = []
            for i in range (0, n):
                if self.frequency[state[i]] >=2 :
                    possible_remove_location.append(i)
            output = []
            for i in possible_remove_location:
                output.append(self.ExTSP_action(i, "remove", None))
            if len(output) == 0:
                print ("too bad")
            return output




    def get_result(self, state, action):
        new_state= state[:]
        if action.action_type == "add":
            index = action.index + 1
            val = action.new_node
            new_state.insert(index , val)
        elif action.action_type == "remove":
            index = action.index
            del new_state[index]

        return new_state


    def select_roulete (self, cls_arr):

        volume = 0.0
        n = len (cls_arr)
        for i in range(0, n):
            volume += cls_arr[i].cost
        rand_value = random.uniform(0, volume)
        for i in cls_arr:
            rand_value -= i.cost
            if (rand_value <= 0):
                return i
        print("problem in finding parent")
        return None

    def modified_cost_array(self, state):
        cost_arr = np.copy(cost1_arr)
        n = len (state)
        for i in range (0,n):
            j = i + 1
            if j == n:
                j = 0
            a= state[i]
            b = state[j]
            cost_arr[(a, b)]= cost2_arr[(a, b)]
            cost_arr[(b, a)] = cost2_arr[(a, b)]
        return cost_arr



    class cost_index:
        def __init__(self, cost, index):
            self.cost = cost
            self.index = index
    class ExTSP_action:
        def __init__(self, index, action_type ,new_node):
            self.index = index
            self.new_node = new_node
            self.action_type = action_type