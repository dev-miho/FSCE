import bisect


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        raise NotImplementedError

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0 if not parent else parent.depth + 1

    def expand(self, problem):
        return [self.child_node(problem, a) for a in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        return Node(
            next_state,
            self,
            action,
            problem.path_cost(self.path_cost, self.state, action, next_state)
        )

    def path(self):
        node, result = self, []
        while node:
            result.append(node)
            node = node.parent
        return list(reversed(result))

    def solution(self):
        return [n.action for n in self.path()[1:]]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


class Queue:
    def append(self, item): raise NotImplementedError
    def extend(self, items): raise NotImplementedError
    def pop(self): raise NotImplementedError


class FIFOQueue(Queue):
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)


def graph_search(problem, fringe):
    closed = set()
    fringe.append(Node(problem.initial))

    while fringe:
        node = fringe.pop()

        if problem.goal_test(node.state):
            return node

        if node.state not in closed:
            closed.add(node.state)
            fringe.extend(node.expand(problem))

    return None


def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue())


def change_direction(d, action):
    if d == "east":
        return {"forward": "east", "backward": "west", "left": "north", "right": "south"}[action]
    if d == "west":
        return {"forward": "west", "backward": "east", "left": "south", "right": "north"}[action]
    if d == "north":
        return {"forward": "north", "backward": "south", "left": "west", "right": "east"}[action]
    return {"forward": "south", "backward": "north", "left": "east", "right": "west"}[action]


class Snake(Problem):
    def __init__(self, initial, red_apples, goal=None):
        super().__init__(initial, goal)
        self.red_apples = set(red_apples)

    def successor(self, state):
        succ = {}

        snake_pos, direction, green_apples = state

        if direction == "south":
            dirs = {"forward": (0, -1), "left": (1, 0), "right": (-1, 0)}
        elif direction == "north":
            dirs = {"forward": (0, 1), "left": (-1, 0), "right": (1, 0)}
        elif direction == "east":
            dirs = {"forward": (1, 0), "left": (0, 1), "right": (0, -1)}
        else:
            dirs = {"forward": (-1, 0), "left": (0, -1), "right": (0, 1)}

        for action, (dx, dy) in dirs.items():
            new_head = (snake_pos[0][0] + dx, snake_pos[0][1] + dy)

            new_snake = list(snake_pos)
            new_snake.insert(0, new_head)
            

            new_direction = change_direction(direction, action)

            new_state = (tuple(new_snake), new_direction, green_apples)

            if self.check_valid(new_state):
                label = f"Move {action}" if action == "forward" else f"Turn {action}"

                if new_head in green_apples:
                    new_green = list(green_apples)
                    new_green.remove(new_head)
                    new_state = (tuple(new_snake), new_direction, tuple(new_green))
                else:
                    new_snake.pop()
                    new_state = (tuple(new_snake), new_direction, green_apples)
                succ[label] = new_state

        return succ

    def check_valid(self, state):
        snake_pos, _, _ = state
        head = snake_pos[0]

        if head in snake_pos[1:]:
            return False
        if head in self.red_apples:
            return False
        if head[0] < 0 or head[0] > 9 or head[1] < 0 or head[1] > 9:
            return False

        return True

    def goal_test(self, state):
        _, _, green = state
        return len(green) == self.goal


if __name__ == '__main__':

    num_green = int(input())
    green_apples = [tuple(map(int, input().split(","))) for _ in range(num_green)]

    num_red = int(input())
    red_apples = [tuple(map(int, input().split(","))) for _ in range(num_red)]

    snake_pos = ((0, 7), (0, 8), (0, 9))
    direction = "south"

    initial_state = (snake_pos, direction, tuple(green_apples))

    problem = Snake(initial_state, red_apples, 0)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No solution!")