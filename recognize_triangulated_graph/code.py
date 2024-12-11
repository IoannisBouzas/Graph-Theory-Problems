from time import sleep

triangulated_graph =   [ 
                       ['A' , 'B'],
                       ['A' , 'C'],
                       ['B' , 'C'],
                       ['B' , 'D'],
                       ['C' , 'D'],
                       ['C' , 'E'],
                       ['D' , 'E']
                       ]


not_triangulated_graph =    [
                            ['A' , 'B'],
                            ['A' , 'C'],
                            ['B' , 'C'],
                            ['B' , 'D'],
                            ['C' , 'E'],
                            ['D' , 'E']
                            ]


def create_adjacency_list(graph):
    adjacency_list = {}
    for edge in graph:
        if edge[0] not in adjacency_list:
            adjacency_list[edge[0]] = [edge[1]]
        else:
            adjacency_list[edge[0]].append(edge[1])
        
        if edge[1] not in adjacency_list:
            adjacency_list[edge[1]] = [edge[0]]
        else:
            adjacency_list[edge[1]].append(edge[0])
    return adjacency_list


def is_triangulated(adjacency_list_copy):
    if len(adjacency_list_copy) == 0:
        return "The package is secure."
    else:
        for v in list(adjacency_list_copy.keys()):
            if is_simplicial(v , adjacency_list_copy):
                for remaining_vertex in adjacency_list_copy:
                    if v in adjacency_list_copy[remaining_vertex]:
                        adjacency_list_copy[remaining_vertex].remove(v)
                adjacency_list_copy.pop(v)
                return is_triangulated(adjacency_list_copy)
        return "The plan was compremised. ABORT MISSION."
    

def is_simplicial(v , adjacency_list_copy):
    for i in(adjacency_list_copy[v]):
        for j in(adjacency_list_copy[v]):
            if i != j and j not in adjacency_list_copy[i]:
                return False
    return True


#main
print("The agent's connections are : " , triangulated_graph)
adjacency_list = create_adjacency_list(triangulated_graph)
sleep(1)
print("Now we have to detect the presence of the possible undermining of the execution of the plan.")
adjacency_list_copy = adjacency_list.copy()
sleep(1)
print("Checking: ", end = '') 
for i in range(4):
    print('.' * (i + 1), end = '')
    sleep(1)
print()
print(is_triangulated(adjacency_list_copy))

print()

print("The agent's connections are : " , not_triangulated_graph)
adjacency_list = create_adjacency_list(not_triangulated_graph)
sleep(1)
print("Now we have to detect the presence of the possible undermining of the execution of the plan.")
adjacency_list_copy = adjacency_list.copy()
sleep(1)
print("Checking: ", end = '') 
for i in range(4):
    print('.' * (i + 1), end = '')
    sleep(1)
print()
print(is_triangulated(adjacency_list_copy))



