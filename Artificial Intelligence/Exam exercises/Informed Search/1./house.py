from searching_framework import Problem, astar_search


def isManAllowed(man_pos, obstacles, n):
    if man_pos in obstacles:
        return False
    if man_pos[0] < 0 or man_pos[1] < 0 or man_pos[0] >= n or man_pos[1] >= n:
        return False
    return True


class House(Problem):
    def __init__(self, initial, obstacles, n, goal):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def successor(self, state):
        succ = {}
        man = state

        dirs = {
            "Up": (0, 1),
            "Down": (0, -1),
            "Left": (-1, 0),
            "Right 2": (2, 0),
            "Right 3": (3, 0),
        }

        for action, (x, y) in dirs.items():
            new_man = (man[0] + x, man[1] + y)

            if action not in ["Right 2", "Right 3"]:
                if isManAllowed(new_man, self.obstacles, self.n):
                    succ[action] = new_man

            elif action == "Right 2":
                if all(
                    isManAllowed((man[0] + i, man[1]), self.obstacles, self.n)
                    for i in range(1, 3)
                ):
                    succ["Right 2"] = (man[0] + 2, man[1])

            elif action == "Right 3":
                if all(
                    isManAllowed((man[0] + i, man[1]), self.obstacles, self.n)
                    for i in range(1, 4)
                ):
                    succ["Right 3"] = (man[0] + 3, man[1])

        return succ


if __name__ == "__main__":
    n = int(input())
    k = int(input())

    obstacles = []
    for i in range(k):
        obstacles.append(tuple(map(int, input().split(","))))

    man = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    problem = House(man, obstacles, n, house)
    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No solution")
