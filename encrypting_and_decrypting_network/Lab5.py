from time import sleep

agent_pairs = [
    
    ["Alpha" , "Charlie"],
    ["Alpha" , "Golf"],
    ["Bravo" , "Delta"],
    ["Delta" , "Alpha"],
    ["Delta" , "Echo"],
    ["Echo" , "Fox"],
    ["Echo" , "Hotel"]

]

agents = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Fox", "Golf", "Hotel"]

agent_to_num = {}

for i, agent in enumerate(agents):
    agent_to_num[agent] = i + 1

adjacency_list = {}

for i in range(len(agents)):
   
    adjacency_list[i+1] = set()

for agent1, agent2 in agent_pairs:
   
    num1 = agent_to_num[agent1]
    num2 = agent_to_num[agent2]

    adjacency_list[num1].add(num2)

    adjacency_list[num2].add(num1)    
    

# Print the graph of the agents
for agent, neighbors in adjacency_list.items():
    print(f"Agent {agent} is connected to agents: {', '.join(map(str, neighbors))}")    



# Making the encoding process
prufer = []
while len(adjacency_list) > 2:
    leaf = min(node for node in adjacency_list if len(adjacency_list[node]) == 1)
    neighbor = adjacency_list[leaf].pop()
    adjacency_list[neighbor].remove(leaf)
    prufer.append(neighbor)
    del adjacency_list[leaf]


#print(prufer)

# Making the encryption process
print("Encrypting Network...")
key = int(input("Enter the secret key: "))

encrypted_result = []
for i in prufer:
    encrypted_result.append(i + key)
    
print()
   
print("The encrypted message that will be transmited is this: " + str(encrypted_result))

print("Decrypting Network...")
decrypt_key = int(input("Enter the secret key to decrypt the message: "))

decrypted_result = []
for i in encrypted_result:
    decrypted_result.append(i - decrypt_key)
    
print("The decrypted message is: " + str(decrypted_result))

print()
sleep(1)
print("Staring Decoding Process...")

helper_array = []
for i in range(len(decrypted_result) + 2):
    helper_array.append(i + 1)


network_tree = []

for x in range(len(decrypted_result)):
    lowest_number_not_included_in_the_Prufer = 0
    for x in helper_array:
        if x not in decrypted_result:
            lowest_number_not_included_in_the_Prufer = x
            break
    
    
    edge = []
    edge.append(lowest_number_not_included_in_the_Prufer)
    edge.append(decrypted_result[0])
    
    decrypted_result.remove(decrypted_result[0])
    decrypted_result.append(lowest_number_not_included_in_the_Prufer)
    
    network_tree.append(edge)
    
edge = []
for x in helper_array:
    if x not in decrypted_result:
        edge.append(x)
        
network_tree.append(edge)

print("The network tree is: " + str(network_tree))  

