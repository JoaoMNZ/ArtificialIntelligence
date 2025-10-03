import json

def greedy_best_first_search(problem):
    def reconstruct_path_with_cost():
        total_cost = 0
        current_state = problem["goal_state"]
        path = [current_state]
        
        while current_state in came_from:
            previous_state = came_from[current_state]
            path.append(previous_state)
            total_cost += problem["state_space"][previous_state][current_state]
            current_state = previous_state

        return path[::-1], total_cost

    current_state = problem["initial_state"]
    explored = {current_state}
    came_from = {}
    while current_state != problem["goal_state"]:
        candidates = {
            state
            for state in problem["state_space"][current_state]
            if state not in explored
        }

        if not candidates:
            return None

        next_state = min(candidates, key=lambda state: problem["heuristic"][state])

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