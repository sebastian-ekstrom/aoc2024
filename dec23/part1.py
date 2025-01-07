import sys
from collections import defaultdict

debug = False
def printd(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

filename = sys.argv[1]
with open(filename) as file:
    lines = [line.strip() for line in file]

connections = set()
connections_per_node = defaultdict(list)

for line in lines:
    node1, node2 = line.split("-")
    connections.add((node1, node2))
    connections.add((node2, node1))
    connections_per_node[node1].append(node2)
    connections_per_node[node2].append(node1)

triangles = set()
for node in connections_per_node:
    if not node.startswith("t"):
        continue
    node_connections = connections_per_node[node]
    for i in range(len(node_connections) - 1):
        for j in range(i+1, len(node_connections)):
            if (node_connections[i], node_connections[j]) in connections:
                triangles.add(tuple(sorted([node, node_connections[i], node_connections[j]])))

printd(triangles)
print(len(triangles))
