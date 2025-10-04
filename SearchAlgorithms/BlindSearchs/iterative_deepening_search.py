import json

def iterative_deepening_search(problem, max_depth):
    def dls_recursive(current_state, depth):
        explored.add(current_state)

        if current_state == goal_state:
            return [goal_state]
        
        if depth == limit:
            return "cutoff"
        
        cutoff_occurred = False
        for neighbor_state in state_space[current_state]:
            if neighbor_state not in explored:
                result = dls_recursive(neighbor_state, depth + 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif isinstance(result, list):
                    return [current_state] + result
            
        return "cutoff" if cutoff_occurred else None
    
    state_space = problem["state_space"]
    initial_state = problem["initial_state"]
    goal_state = problem["goal_state"]
    
    for limit in range(max_depth + 1):
        explored = set()
        result = dls_recursive(initial_state, 0)
        if result != "cutoff":
            return result
    
    return "cutoff"

def main():
    with open("romania_problem.json", "r") as file:
        problem = json.load(file)

    max_depth = 5
    solution = iterative_deepening_search(problem, max_depth)
    if solution == "cutoff":
        print(f"No path found within depth limit of {max_depth}. Deeper path may exist.")
    elif isinstance(solution, list):
        formatted_path = " -> ".join(solution)
        print(f"Path from {problem["initial_state"]} to {problem["goal_state"]}: {formatted_path}\nTotal path cost: {len(solution) - 1}")
    else:
        print(f"No path could be found from {problem['initial_state']} to {problem['goal_state']}.")

if __name__ == "__main__":
    main()