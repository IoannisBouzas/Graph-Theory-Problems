from time import sleep

strongly_connected_graph = [ 
                       ['A' , 'B'],
                       ['B' , 'C'],
                       ['C' , 'D'],
                       ['D' , 'E'],
                       ['E' , 'A']
                       ]


not_strongly_connected_graph = [
                            ['A' , 'B'],
                            ['A' , 'C'],
                            ['B' , 'C'],
                            ['C' , 'D'],
                            ['D' , 'C']
                            ]


def create_adjacency_list(graph):
    adjacency_list = {}
    for edge in graph:
        if edge[0] not in adjacency_list:
            adjacency_list[edge[0]] = [edge[1]]
        else:
            adjacency_list[edge[0]].append(edge[1])
    return adjacency_list


def DFS(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)


def reverse_graph(graph):
    reversed_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor in reversed(graph[node]):
            reversed_graph[neighbor].append(node)
    return reversed_graph



def is_strongly_connected(graph):

    visited = set()
    DFS(graph, list(graph.keys())[0], visited)

    if len(visited) == len(graph):
        reversed_graph = reverse_graph(graph)
        visited = set()
        DFS(reversed_graph, list(graph.keys())[0], visited)
        if len(visited) == len(graph):
            return "The graph is strongly connected"

    return "The graph is not strongly connected"


#main
print("The connections between royal entourage are as follows: " + str(strongly_connected_graph))
adjacency_list = create_adjacency_list(strongly_connected_graph)
print("The graph that represent the connections: " + str(adjacency_list))
sleep(1)
print("Connection status.....")
sleep(1)
print(is_strongly_connected(adjacency_list))

print()

print("The connections between royal entourage are as follows: " + str(not_strongly_connected_graph))
adjacency_list = create_adjacency_list(not_strongly_connected_graph)
print("The graph that represent the connections: " + str(adjacency_list))
sleep(1)
print("Connection status.....")
sleep(1)
print(is_strongly_connected(adjacency_list))

