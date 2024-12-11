import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def find_shortest_path(graph):
    min_risk = float('inf')
    shortest_path = None
    
    for start_node in graph:
        distances = dijkstra(graph, start_node)
        total_risk = sum(distances.values())
        if total_risk < min_risk:
            min_risk = total_risk
            shortest_path = distances
    
    return shortest_path

def build_graph(data):
    graph = {}
    for line in data:
        source, destination, risk = line.split(', ')
        risk = int(risk)
        if source not in graph:
            graph[source] = {}
            
        graph[source][destination] = risk
    print(graph)
    return graph

data = [
    "ALPHA, BRAVO, 13",
    "ALPHA, CHARLIE, 51",
    "ALPHA, FOXTROT, 70",
    "ALPHA, DELTA, 68",
    "ALPHA, ECHO, 51",
    "BRAVO, ALPHA, 13",
    "BRAVO, CHARLIE, 60",
    "BRAVO, FOXTROT, 70",
    "BRAVO, DELTA, 68",
    "BRAVO, ECHO, 61",
    "CHARLIE, ALPHA, 51",
    "CHARLIE, BRAVO, 60",
    "CHARLIE, FOXTROT, 56",
    "CHARLIE, DELTA, 35",
    "CHARLIE, ECHO, 2",
    "FOXTROT, ALPHA, 70",
    "FOXTROT, BRAVO, 70",
    "FOXTROT, CHARLIE, 56",
    "FOXTROT, DELTA, 21",
    "FOXTROT, ECHO, 57",
    "DELTA, ALPHA, 68",
    "DELTA, BRAVO, 68",
    "DELTA, CHARLIE, 35",
    "DELTA, FOXTROT, 21",
    "DELTA, ECHO, 36",
    "ECHO, ALPHA, 51",
    "ECHO, BRAVO, 61",
    "ECHO, CHARLIE, 2",
    "ECHO, FOXTROT, 57",
    "ECHO, DELTA, 36"
]

graph = build_graph(data)
shortest_path = find_shortest_path(graph)
print("Shortest path with minimum risk:")
for destination, risk in shortest_path.items():
    print(f"To {destination} - Risk: {risk}")
