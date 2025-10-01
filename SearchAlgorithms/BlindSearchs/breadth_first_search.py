import json
from collections import deque

def breadth_first_search(graph, start_node, goal_node):
    if start_node == goal_node:
        return start_node
    
    reached = {start_node}
    frontier = deque([start_node])
    while frontier:
        current_node = frontier.popleft()
        for child in graph[current_node]:
            if child == goal_node:
                return child
            if child not in reached:
                reached.add(child)
                frontier.append(child)
    return None

def main():
    with open("romenia.json", "r") as file:
        data = json.load(file)

    graph = data["edges"]
    initial_state = data["initial_state"]
    goal = data["goal"]
   
    result = breadth_first_search(graph, initial_state, goal)
    if result:
        print(goal, "is reachable.")
    else:
        print(goal, "is not reachable.")
        
if __name__ == "__main__":
    main()