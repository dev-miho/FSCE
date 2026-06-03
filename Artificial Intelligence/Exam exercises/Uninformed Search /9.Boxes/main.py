from searching_framework import *


class Boxes(Problem):
    def __init__(self, initial, n, boxes, goal):
        super().__init__(initial, goal)
        self.n = n
        self.boxes = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        _, _, filled = state
        return all(filled)

    def successor(self, state):
        succ = {}

        dirs = {
            "Gore": (0, 1),
            "Desno": (1, 0)
        }

        man_pos, num_boxes, filled = state

        for action, (dx, dy) in dirs.items():

            new_man_pos = (man_pos[0] + dx, man_pos[1] + dy)

            if not self.check_valid(new_man_pos):
                continue

            new_filled = list(filled)
            new_num = num_boxes

            
            for i, box in enumerate(self.boxes):
                if not new_filled[i]:
                    if max(abs(new_man_pos[0] - box[0]),
                           abs(new_man_pos[1] - box[1])) == 1:
                        new_filled[i] = True
                        new_num -= 1

            succ[action] = (
                new_man_pos,
                new_num,
                tuple(new_filled)
            )

        return succ

    def check_valid(self, man_pos):
        x, y = man_pos

        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            return False

        if man_pos in self.boxes:
            return False

        return True


if __name__ == '__main__':
    n = int(input())

    man_pos = (0, 0)

    num_boxes = int(input())

    boxes = []
    filled = []

    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))
        filled.append(False)

    initial_state = (man_pos, num_boxes, tuple(filled))

    problem = Boxes(initial_state, n, boxes, num_boxes)

    result = breadth_first_graph_search(problem)

    if result is None:
        print("No Solution!")
    else:
        print(result.solution())