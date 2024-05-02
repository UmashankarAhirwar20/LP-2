def bfs(graph, initial):
    visited = []
    queue = [initial]
    
    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            visited.append(node)
            
            neighbours = graph.get(node, [])
            for neighbour in neighbours:
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)
                    
    return visited

# Define the graph
graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

# Test the BFS function starting from node 'A'
print(bfs(graph, 'A'))
