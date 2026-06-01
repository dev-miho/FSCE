from searching_framework import *


class Robot(Problem):
    def __init__(self, initial, M1_pos, M1_steps, M2_pos, M2_steps, walls, goal=None):
        super().__init__(initial, goal)
        self.M1_pos = M1_pos
        self.M1_steps = M1_steps
        self.M2_pos = M2_pos
        self.M2_steps = M2_steps
        self.walls = set(walls)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        _, _, _, isFixedM1, isFixedM2, _, _ = state
        return isFixedM1 and isFixedM2

    def check_valid(self, pos):
        x, y = pos

        if x < 0 or x > 9 or y < 0 or y > 9:
            return False

        if pos in self.walls:
            return False

        return True

    def successor(self, state):
        succ = {}

        robot_pos, to_collect_M1, to_collect_M2, isFixedM1, isFixedM2, count1, count2 = state

        directions = {
            "Up": (0, 1),
            "Down": (0, -1),
            "Left": (-1, 0),
            "Right": (1, 0)
        }

        # MOVE ACTIONS
        for action, (dx, dy) in directions.items():
            new_pos = (robot_pos[0] + dx, robot_pos[1] + dy)

            if not self.check_valid(new_pos):
                continue

            new_to_collect_M1 = to_collect_M1
            new_to_collect_M2 = to_collect_M2

            
            new_count1 = 0 if not isFixedM1 else count1
            new_count2 = 0 if not isFixedM2 else count2

   
            if new_pos in to_collect_M1 and not isFixedM1:
                temp = list(to_collect_M1)
                temp.remove(new_pos)
                new_to_collect_M1 = tuple(temp)

            if new_pos in to_collect_M2 and isFixedM1 and not isFixedM2:
                temp = list(to_collect_M2)
                temp.remove(new_pos)
                new_to_collect_M2 = tuple(temp)

            succ[action] = (
                new_pos,
                new_to_collect_M1,
                new_to_collect_M2,
                isFixedM1,
                isFixedM2,
                new_count1,
                new_count2
            )

        
        if (
            robot_pos == self.M1_pos and
            len(to_collect_M1) == 0 and
            not isFixedM1
        ):
            new_count1 = count1 + 1

            succ["Repair"] = (
                robot_pos,
                to_collect_M1,
                to_collect_M2,
                new_count1 >= self.M1_steps,
                isFixedM2,
                new_count1,
                count2
            )

        
        if (
            robot_pos == self.M2_pos and
            isFixedM1 and
            len(to_collect_M2) == 0 and
            not isFixedM2
        ):
            new_count2 = count2 + 1

            succ["Repair"] = (
                robot_pos,
                to_collect_M1,
                to_collect_M2,
                isFixedM1,
                new_count2 >= self.M2_steps,
                count1,
                new_count2
            )

        return succ


if __name__ == '__main__':
    robot_start_pos = tuple(map(int, input().split(',')))
    M1_pos = tuple(map(int, input().split(',')))
    M1_steps = int(input())
    M2_pos = tuple(map(int, input().split(',')))
    M2_steps = int(input())
    parts_M1 = int(input())
    to_collect_M1 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M1)])
    parts_M2 = int(input())
    to_collect_M2 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M2)])
    
    walls = [(4,0),(5,0),(7,5),(8,5),(9,5),(1,6),(1,7),(0,6),(0,8),(0,9),(1,9),(2,9),(3,9)]
    
    initial_state=(robot_start_pos,to_collect_M1,to_collect_M2,False,False,0,0)
    problem = Robot(initial_state,M1_pos,M1_steps,M2_pos,M2_steps,walls,True)

    result = breadth_first_graph_search(problem)
    
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
