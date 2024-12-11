from time import sleep

agents = ["Alpha" , "Bravo" , "Charlie" , "Delta" , "Echo" , "Fox"]

connections = [
    ["Alpha" ,"Bravo"] , ["Alpha" ,"Delta"] , ["Alpha" ,"Echo"] , ["Alpha" ,"Fox"],
    ["Bravo","Alpha"] , ["Bravo","Fox"],
    ["Charlie" , "Delta"],
    ["Delta", "Alpha"] , ["Delta" ,"Charlie"] ,["Delta" ,"Echo"], 
    ["Echo" , "Alpha"] , ["Echo" ,"Delta"],
    ["Fox" , "Alpha"] , ["Fox" ,"Bravo"]    
]

def dfs(agent, visited , connections , component):
    print(f"Visiting agent {agent}...")
    visited.add(agent)
    component.append(agent)
    sleep(1)

    for connection in connections:
        if agent == connection[0]:  
            neighbor = connection[1]  
            if neighbor not in visited:
                print(f"Agent {agent} is connected to agent {neighbor}")
                dfs(neighbor, visited, connections, component)


def find_connected_components(agents, connections):
    print("\nBuilding network...")
    connected_components = []
    visited = set()

    for agent in agents:
        if agent not in visited:
            print(f"\nStarting new component with agent {agent}")
            component = []
            dfs(agent, visited, connections, component)
            connected_components.append(component)
            print(f"Finished building component: {component}")
            sleep(1)
            
    print(f"\nFinal network: {connected_components}")
    return connected_components




def is_coherent(component, connections):
    print(f"\nChecking network coherence...")
    for agent in component:
        temp_component = [a for a in component if a != agent]
        temp_connections = [c for c in connections if agent not in c]
        temp_connected_components = find_connected_components(temp_component, temp_connections)
        if len(temp_connected_components) > 1:
            print(f"\nRemoving agent {agent} makes the network not coherent. This agent is crucial for message transfer")
        else:
            print(f"\nRemoving agent {agent} does not affect the coherence of the network")
        sleep(1)
   

#main  
print("Initializing network...")
sleep(1)
connected_components = find_connected_components(agents, connections)
    
for component in connected_components:
    is_coherent(component, connections)

