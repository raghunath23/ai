import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0  

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    return ((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2) ** 0.5

def astar(maze, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movements: right, left, down, up

        for neighbor in neighbors:
            new_position = (current_node.position[0] + neighbor[0], current_node.position[1] + neighbor[1])

            if (
                new_position[0] < 0
                or new_position[0] >= len(maze)
                or new_position[1] < 0
                or new_position[1] >= len(maze[0])
                or maze[new_position[0]][new_position[1]] == 1
                or new_position in closed_set
            ):
                continue

            new_node = Node(new_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = heuristic(new_position, goal_node.position)
            new_node.f = new_node.g + new_node.h

            if new_node not in open_set:
                heapq.heappush(open_set, new_node)

    return None  

maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start_position = (0, 0)
goal_position = (4, 4)

path = astar(maze, start_position, goal_position)
print("A* Path:", path)
