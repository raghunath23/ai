def is_valid_assignment(graph, vertex, color, assignment):
    for neighbor in graph[vertex]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtrack(graph, assignment, colors, current_vertex):
    if current_vertex not in graph:
        return assignment
    for color in colors:
        if is_valid_assignment(graph, current_vertex, color, assignment):
            assignment[current_vertex] = color
            result = backtrack(graph, assignment.copy(), colors, next_vertex(graph, assignment))
            if result is not None:
                return result
    return None
def next_vertex(graph, assignment):
    for vertex in graph:
        if vertex not in assignment:
            return vertex
    return None
def color_graph(graph, colors):
    assignment = {}
    start_vertex = next(iter(graph))
    return backtrack(graph, assignment, colors, start_vertex)
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    available_colors = ['Red', 'Green', 'Blue']
    solution = color_graph(graph, available_colors)
    if solution is not None:
        print("Solution found:")
        for vertex, color in solution.items():
            print(f"{vertex}: {color}")
    else:
        print("No solution found.")

"""
Sample output
Solution found:
A: Red
B: Green
C: Blue
D: Red
"""
