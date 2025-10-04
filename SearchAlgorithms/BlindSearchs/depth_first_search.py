import json

def depth_first_search(problem):
    def dfs_recursive(current_state):
        explored.add(current_state)

        if current_state == goal_state:
            return [goal_state]

        for neighbor_state in state_space[current_state]:
            if neighbor_state not in explored:
                result = dfs_recursive(neighbor_state)
                if result:
                    return [current_state] + result
            
        return None
    
    state_space = problem["state_space"]
    initial_state = problem["initial_state"]
    goal_state = problem["goal_state"]
    explored = set()

    path = dfs_recursive(initial_state)
    if path:
        return path, len(path) - 1
    return None

def main():
    with open("romania_problem.json", "r") as file:
        problem = json.load(file)

    solution = depth_first_search(problem)
    if solution:
        path, total_cost = solution
        formatted_path = " -> ".join(path)
        print(f"Path from {problem["initial_state"]} to {problem["goal_state"]}: {formatted_path}\nTotal path cost: {total_cost}")
    else:
        print(f"No path could be found from {problem['initial_state']} to {problem['goal_state']}.")

if __name__ == "__main__":
    main()