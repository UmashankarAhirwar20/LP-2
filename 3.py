INF = 9999999
N = 5  # Number of vertices in the graph

# Creating the graph using an adjacency matrix
G = [
    [0, 19, 5, INF, INF],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [INF, 9, 1, 0, 1],
    [INF, 2, 6, 1, 0]
]

# Initialize the selected_node list to track which nodes are selected in MST
selected_node = [False] * N
# Start with the first node selected in MST
selected_node[0] = True

# Initialize the count of edges in MST
no_edge = 0

print("Edge : Weight")

# Iterate until the number of edges in MST is less than the number of vertices - 1
while no_edge < N - 1:
    # Initialize minimum weight to INF
    minimum = INF
    # Initialize variables to store the selected edge
    a = -1
    b = -1
    
    # Iterate through the selected nodes
    for m in range(N):
        if selected_node[m]:
            # Iterate through the neighbors of the selected node
            for n in range(N):
                # If the neighbor is not selected and there is an edge
                if not selected_node[n] and G[m][n] < minimum:
                    # Update the minimum edge
                    minimum = G[m][n]
                    a = m
                    b = n
    
    # If a valid edge is found, add it to the MST
    if a != -1 and b != -1:
        print(f"{a} - {b} : {G[a][b]}")
        # Mark the new node as selected
        selected_node[b] = True
        # Increment the edge count
        no_edge += 1
