import json

def greedy_best_first_search(problem):
    def reconstruct_path_with_cost():
        path = [goal_state]
        total_cost = 0

        current_state = goal_state
        while current_state in came_from:
            previous_state = came_from[current_state]
            path.append(previous_state)
            total_cost += state_space[previous_state][current_state]
            current_state = previous_state

        return path[::-1], total_cost

    state_space = problem["state_space"]
    initial_state = problem["initial_state"]
    goal_state = problem["goal_state"]
    h_costs = problem["heuristic"]
    explored = set()
    came_from = {}
    
    explored.add(initial_state)
    current_state = initial_state
    while current_state != goal_state:
        candidates = {
            neighbor_state
            for neighbor_state in state_space[current_state]
            if neighbor_state not in explored
        }

        if not candidates:
            return None

        next_state = min(candidates, key=lambda candidate: h_costs[candidate])

        came_from[next_state] = current_state
        explored.add(next_state)
        current_state = next_state

    return reconstruct_path_with_cost()
    
def main():
    with open("romania_problem.json", "r") as file:
        problem = json.load(file)

    solution = greedy_best_first_search(problem)
    if solution:
        path, total_cost = solution
        formatted_path = " -> ".join(path)
        print(f"Path from {problem["initial_state"]} to {problem["goal_state"]}: {formatted_path}\nTotal path cost: {total_cost}")
    else:
        print(f"No path could be found from {problem['initial_state']} to {problem['goal_state']}.")

if __name__ == "__main__":
    main()