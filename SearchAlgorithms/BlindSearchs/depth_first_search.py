import json

def depth_first_search(graph, start_node, goal_node):
    reachable = set()
    
    def dfs_recursive(current_node):
        if current_node in reachable:
            return None
        reachable.add(current_node)

        if current_node == goal_node:
            return current_node

        for child in graph[current_node]:
            found_node = dfs_recursive(child)
            if found_node:
                return found_node
            
        return None

    return dfs_recursive(start_node)

def main():
    with open("romenia.json", "r") as file:
        data = json.load(file)

    graph = data["edges"]
    initial_state = data["initial_state"]
    goal = data["goal"]
   
    result = depth_first_search(graph, initial_state, goal)
    if result:
        print(goal, "is reachable.")
    else:
        print(goal, "is not reachable.")
        
if __name__ == "__main__":
    main()