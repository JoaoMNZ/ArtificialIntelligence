import json
from collections import defaultdict
import heapq

def uniform_cost_search(problem):
    def reconstruct_path():
        current_state = goal_state
        path = [current_state]
        while current_state in came_from:
            current_state = came_from[current_state]
            path.append(current_state)

        return path[::-1]
    
    state_space = problem["state_space"]
    initial_state = problem["initial_state"]
    goal_state = problem["goal_state"]
    g_costs = defaultdict(lambda: float('inf'))
    came_from = {}

    g_costs[initial_state] = 0
    frontier = [(g_costs[initial_state], initial_state)]
    while frontier:
        current_g_cost, current_state = heapq.heappop(frontier)

        if current_g_cost > g_costs[current_state]:
            continue

        if current_state == goal_state:
            return reconstruct_path(), g_costs[goal_state]
        
        for neighbor_state, neighbor_weight in state_space[current_state].items():
            new_g_cost = current_g_cost + neighbor_weight
            if new_g_cost < g_costs[neighbor_state]:
                g_costs[neighbor_state] = new_g_cost
                came_from[neighbor_state] = current_state
                heapq.heappush(frontier, (new_g_cost, neighbor_state))
    
    return None

def main():
    with open("romania_problem.json", "r") as file:
        problem = json.load(file)

    solution = uniform_cost_search(problem)
    if solution:
        path, total_cost = solution
        formatted_path = " -> ".join(path)
        print(f"Path from {problem["initial_state"]} to {problem["goal_state"]}: {formatted_path}\nTotal path cost: {total_cost}")
    else:
        print(f"No path could be found from {problem['initial_state']} to {problem['goal_state']}.")

if __name__ == "__main__":
    main()