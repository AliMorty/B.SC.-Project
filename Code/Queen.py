from random import randint
from ProblemFile import ProblemClass

gameSize = 8
class QueenProblem(ProblemClass):

    def get_initial_state(self):
        arr = []
        for i in range( 0 , gameSize):
            arr.append(i)
        # for i in range (0 , gameSize):
        #     print(arr[i])
        return QueenState(arr)
    def get_initial_state_random(self):
        arr = []
        for i in range( 0 , gameSize):
            arr.append(-1)
        for i in range (0 , gameSize):
            rand = randint(0,7-i)
            count=0
            for j in range (0, gameSize):
                if arr[j]==-1:
                    if count == rand:
                        arr[j] = i
                        break
                    if count != rand:
                            count += 1

        return QueenState(arr)
    def get_actions(self, state):
       # print ("This is a test!")
        return state.get_actions()
    def get_result(self, state, action):
        arr = list(state.arr)
        i= action.first
        j= action.second
        tmp=arr[i]
        arr[i]=arr[j]
        arr[j]=tmp
        return QueenState(arr)
    def is_goal(self, state):
        return state.is_goal()
    def get_score(self, state):
        return state.get_score()
    def get_cost(self, state, action):
        return 1
    def is_equal(self, state1, state2):
        return state1.is_equal(state2)
    def show_state(self, state):
        state.show_state()



class QueenState():
    def __init__(self, initialArr):
        self.arr = initialArr
        return
    def get_actions (self):
        actions = []
        for i in range (0, gameSize):
            for j in range (i+1, gameSize):
                actions.append(QueenAction(i, j))
     #   print("actions", len(actions))
        return actions
    def is_goal(self):
        for i in range (0 , gameSize):
            for j in range (i+1, gameSize):
                if (abs(self.arr[j]-self.arr[i])==j-i):
                    return False
        return True
    def get_score(self):
        score=0
        for i in range (0 , gameSize):
            for j in range (i+1, gameSize):
                if (abs(self.arr[j]-self.arr[i])==j-i):
                    score+=1
        score=-score
        return score
    def is_equal (self, s):
        arr = s.arr
        for i in range (0 , gameSize):
            if self.arr[i] !=arr[i]:
                return False
        return True
    def show_state(self):
        # for i in range (0 , gameSize):
        #     for j in range (0, gameSize):
        #         if (self.arr[i]==j):
        #             print ("#", end='')
        #         else:
        #             print ("-", end='')
        #     print()
        print("[", end='')
        for i in range (0, gameSize -1 ):
            print (self.arr[i], ",", end='')
        print(self.arr[gameSize-1],"]")



class QueenAction():
    def __init__(self, first, second):
        self.first= first
        self.second=second
        return






