#IOANNIS MPOUZAS AM: 5025

#floyd_warshall algorithm to find the shortest path between all pairs of vertices in the graph
def floyd_warshall(graph):
    n = len(graph)
    dist = graph
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


#find_median_center function to find the median and center of the graph
def find_median_center(dist):
    total_distances = [sum(row) for row in dist]
    max_distances = [max(row) for row in dist]
    print(f"The total distances from each vertex to all other vertices are: {total_distances}")
    print(f"The maximum distances from each vertex to any other vertex are: {max_distances}")

    median = total_distances.index(min(total_distances))
    center = max_distances.index(min(max_distances))

    print(f"The median of the graph is the vertex with the minimum distance: {median}")
    print(f"The center of the graph is the vertex with the minimum maximum distance: {center}")

    return median, center



# main
# Initialize graph with infinities for all edges
inf = float('inf')
graph = [[inf] * 8 for i in range(8)]

# We add edges
graph[0][3]=1
graph[1][7]=1
graph[2][3]=1
graph[3][0]=1
graph[3][2]=1
graph[3][4]=1
graph[3][5]=1
graph[3][6]=1
graph[4][3]=1
graph[5][3]=1
graph[6][3]=1
graph[6][7]=1
graph[7][1]=1
graph[7][6]=1

# Set diagonal to 0
for i in range(8):
    graph[i][i] = 0



distances = floyd_warshall(graph)
median, center = find_median_center(distances)

print(f"We should place the pharmacy at the center of the graph which is vertex: {center}")
print(f"We should place the hospital at the median of the graph which is vertex: {median}")

