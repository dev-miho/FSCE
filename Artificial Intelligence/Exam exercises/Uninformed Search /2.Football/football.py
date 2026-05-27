from searching_framework import Problem, breadth_first_graph_search #, just an example, import whatever you actually need from the searching framework
# note that your program won't work if you copy paste classes instead of import them via the above statement

# define your Problem class here

class Football(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def actions(self, state):
        return self.successor(state).keys()
       
    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        
        _,ball_pos=state
        
        return ball_pos in self.goal
    
    def successor(self, state):
        
        succ={}
        
        return succ
    
    @staticmethod
    def check_valid(state):
        
        
        return True

if __name__ == '__main__':
    
    man_pos=tuple(map(int,input().split(",")))
    ball_pos=tuple(map(int,input().split(",")))