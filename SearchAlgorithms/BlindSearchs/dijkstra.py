import json
from collections import defaultdict
import heapq

def dijkstra(graph, source):
    distances = defaultdict(lambda: float('inf'))
    predecessors = {}

    distances[source] = 0
    priority_queue = [(distances[source], source)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, source, destination):
    path = []

    if destination in predecessors or destination == source:
        current_node = destination
        while current_node is not None:
            path.append(current_node)
            current_node = predecessors.get(current_node)

    return path[::-1]

def main():
    with open("romania_graph.json", "r") as file:
        data = json.load(file)
    source = data["source"]
    destination = data["destination"]
    graph = data["graph"]

    distances, predecessors = dijkstra(graph, source)
    path = reconstruct_path(predecessors, source, destination)

    formatted_path = " -> ".join(path)
    total_distance = distances[destination]
    print(f"Path from {source} to {destination}: {formatted_path}\nTotal distance: {total_distance}")

if __name__ == "__main__":
    main()