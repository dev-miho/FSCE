from searching_framework import *


class Laser(Problem):
    def __init__(self, initial,N,M,blocked,goal=None):
        super().__init__(initial, goal)
        self.N=N
        self.M=M
        self.blocked=blocked

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man,_,_=state
        return man == self.goal

    def successor(self, state):
        succ={}
        
        man,timer,laser=state
        dirs={"Gore":(0,+1),"Dolu":(0,-1),"Levo":(-1,0),"Desno":(+1,0),"Stoj":(0,0)}
        
        for dir,(x,y) in dirs.items():
            new_man=(man[0]+x,man[1]+y)
            new_timer= 1 if timer >= 4 else timer+1
            
            new_laser=new_man if new_timer == 1 else laser
            
            if self.check_valid((new_man,new_timer,new_laser)):
                succ[dir]=(new_man,new_timer,new_laser)
                
        
        return succ
    
    def check_valid(self,state):
        man,timer,laser=state
        
        if man[0]<0 or man[0]>=self.M or man[1]<0 or man[1]>=self.N:
            return False
        if man in self.blocked:
            return False
        if timer == 4 and (man[0] == laser[0] or man[1] == laser[1]):
            return False
        return True
            
            
        


read_two = lambda: tuple(map(int, input().split()))
if __name__ == '__main__':
    N, M = read_two()
    man_pos = read_two()
    target_pos = read_two()
    timer = int(input())
    laser_pos = read_two()
    blocked = [read_two() for _ in range(int(input()))]
    
    
    initial_state=(man_pos,timer,laser_pos)
    problem=Laser(initial_state,N,M,blocked,target_pos)

    result = breadth_first_graph_search(problem)
    
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
