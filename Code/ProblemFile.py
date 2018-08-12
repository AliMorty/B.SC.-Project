class ProblemClass:
    def get_initial_state_random(self):
        pass
    def get_initial_state(self):
        pass
    def get_actions(self, state):
        pass
    def get_result(self, state, action):
        pass
    def is_goal(self, state):
        pass
    def get_cost(self, state, action):
        pass
    def get_score(self, state):
        pass
    def is_equal(self, state1, state2):
        pass
    def show_state(self, state):
        pass
    def return_state(self, state):
        pass
    def mutate(self, x, mean, var):
        pass
    def reproduce(self, state1, state2):
        pass
    def fitness (self, state):
        pass
    def cost (self, state):
        pass
