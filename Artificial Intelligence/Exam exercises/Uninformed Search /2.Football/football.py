from searching_framework import Problem, breadth_first_graph_search #, just an example, import whatever you actually need from the searching framework
# note that your program won't work if you copy paste classes instead of import them via the above statement

# define your Problem class here

class Football(Problem):
    def __init__(self, initial,defenders,goal=None):
        super().__init__(initial, goal)
        self.defenders=defenders

    def actions(self, state):
        return self.successor(state).keys()
       
    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        
        _,ball_pos=state
        
        return ball_pos in self.goal
    
    def successor(self, state):
        
        succ={}
        man_pos,ball_pos=state
        directions={
            "up":(0,1),
            "down":(0,-1),
            "right":(1,0),
            "up-right":(1,1),
            "down-right":(1,-1),
        }
        for direction,(x,y) in directions.items():
            new_man_pos=(man_pos[0]+x,man_pos[1]+y)
            if self.check_valid((new_man_pos,ball_pos)):
                if new_man_pos != ball_pos:
                     succ[f"Move man {direction}"]=(new_man_pos,ball_pos)
                if new_man_pos == ball_pos:
                    new_ball_pos=(ball_pos[0]+x,ball_pos[1]+y)
                    if self.check_valid((new_man_pos,new_ball_pos)):
                        succ[f"Push ball {direction}"]=(new_man_pos,new_ball_pos)
                
        return succ
    
    @staticmethod
    def check_valid(state):
        man_pos,ball_pos=state
        
        for defender in defenders:
            if abs(defender[0]-ball_pos[0])<=1 and abs(defender[1]-ball_pos[1])<=1:
                return False
            
        if man_pos in defenders:
            return False
        
        if man_pos[0]<0 or man_pos[0]>7 or man_pos[1]<0 or man_pos[1]>5:
            return False
        
        if ball_pos[0]<0 or ball_pos[0]>7 or ball_pos[1]<0 or ball_pos[1]>5:
            return False
            
        
        
        return True

if __name__ == '__main__':
    
    defenders=[(3,3),(5,4)]
    goal=[(7,2),(7,3)]
    man_pos=tuple(map(int,input().split(",")))
    ball_pos=tuple(map(int,input().split(",")))
    
    initial_state=(man_pos,ball_pos)
    problem=Football(initial_state,defenders,goal)
    
    solution=breadth_first_graph_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("No Solution!")
    
    