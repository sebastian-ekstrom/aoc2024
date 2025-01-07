import sys
from collections import deque

debug = True
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

def possible_expansions(subgraph, connections, nbr_nodes):
    expansions = []
    for new_node in range(max(subgraph) + 1, nbr_nodes):
        connected = True
        for old_node in subgraph:
            if (old_node, new_node) not in connections:
                connected = False
                break
        if connected:
            expansions.append(new_node)
    return expansions

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

connections = set()
nodes = set()
for line in lines:
    node1, node2 = line.split("-")
    nodes.add(node1)
    nodes.add(node2)
    connections.add((node1, node2))
    connections.add((node2, node1))

sorted_nodes = list(sorted(nodes))
index_connections = set()
for node1, node2 in connections:
    index1 = sorted_nodes.index(node1)
    index2 = sorted_nodes.index(node2)
    if index1 < index2:
        index_connections.add((index1, index2))

largest_subgraph = []
for node1, node2 in index_connections:
    subgraphs = deque([[node1, node2]])
    while len(subgraphs) > 0:
        subgraph = subgraphs.popleft()
        if len(subgraph) > len(largest_subgraph):
            largest_subgraph = subgraph[:]
        expansions = possible_expansions(subgraph, index_connections, len(nodes))
        for node in expansions:
            next_subgraph = subgraph[:]
            next_subgraph.append(node)
            subgraphs.append(next_subgraph)

print(",".join([sorted_nodes[i] for i in largest_subgraph]))
