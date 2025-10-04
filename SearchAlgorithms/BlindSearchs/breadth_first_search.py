import json
from collections import deque

def breadth_first_search(problem):
    def reconstruct_path_with_cost():
        path = [goal_state]

        current_state = goal_state
        while current_state in came_from:
            current_state = came_from[current_state]
            path.append(current_state)

        return path[::-1], len(path) - 1

    state_space = problem["state_space"]
    initial_state = problem["initial_state"]
    goal_state = problem["goal_state"]
    explored = set()
    came_from = {}

    explored.add(initial_state)
    frontier = deque([initial_state])
    while frontier:
        current_state = frontier.popleft()

        if current_state == goal_state:
            return reconstruct_path_with_cost()

        for neighbor_state in state_space[current_state]:
            if neighbor_state not in explored:
                explored.add(neighbor_state)
                came_from[neighbor_state] = current_state
                frontier.append(neighbor_state)
   
    return None

def main():
    with open("romania_problem.json", "r") as file:
        problem = json.load(file)

    solution = breadth_first_search(problem)
    if solution:
        path, total_cost = solution
        formatted_path = " -> ".join(path)
        print(f"Path from {problem["initial_state"]} to {problem["goal_state"]}: {formatted_path}\nTotal path cost: {total_cost}")
    else:
        print(f"No path could be found from {problem['initial_state']} to {problem['goal_state']}.")

if __name__ == "__main__":
    main()