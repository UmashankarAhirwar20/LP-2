import queue as Q

# Define the graph (edge costs) and heuristic values
dict_gn = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Bucharest': {'Urziceni': 85, 'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu': 146},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Oradea': 71, 'Arad': 75}
}

dict_hn = {
    'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

def astar_search(start, goal):
    # PriorityQueue with (total cost, path list, current city)
    cityq = Q.PriorityQueue()
    cityq.put((0 + dict_hn[start], [start], start))
    visited = set()

    while not cityq.empty():
        total_cost, path, current_city = cityq.get()

        # If we reach the goal, return the path and cost
        if current_city == goal:
            return path, total_cost

        # If the city has been visited, skip it
        if current_city in visited:
            continue

        # Mark the city as visited
        visited.add(current_city)

        # Expand the current city to its neighbors
        for neighbor, cost in dict_gn[current_city].items():
            if neighbor not in visited:
                # Calculate the new path cost
                new_cost = total_cost - dict_hn[current_city] + cost + dict_hn[neighbor]
                # Append the neighbor to the path
                new_path = path + [neighbor]
                # Add the new path, cost, and city to the priority queue
                cityq.put((new_cost, new_path, neighbor))

    # If no path is found, return None
    return None, None

if __name__ == "__main__":
    start = 'Arad'
    goal = 'Bucharest'
    path, total_cost = astar_search(start, goal)
    if path:
        print(f"The A* path from {start} to {goal} is: {' -> '.join(path)}")
        print(f"Total cost: {total_cost}")
    else:
        print(f"No path found from {start} to {goal}.")
