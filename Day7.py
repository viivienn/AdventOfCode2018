import networkx as nx
from string import ascii_uppercase

file = open("input_d7.txt").read().splitlines()

#Challenge 1
# Creation of directed graph with edges from the instructions

Graph = nx.DiGraph()

for line in file:
    Graph.add_edges_from([(line.split()[1], line.split()[7])])
order = ''.join(nx.lexicographical_topological_sort(Graph))

print("Order :" + str(order))


# Challenge 2
totalTime = 0
worker = {}

while Graph:
    steps = [x for x in Graph if Graph.in_degree(x) == 0]

    for i in steps:
        if i not in worker:
            worker[i] = ord(i) - ord('A') + 61

    totalTime += min(worker.values())
    worker = {k: v-min(worker.values()) for k,v in worker.items()}

    remove = []

    for i in worker:
        if worker[i] == 0:
            Graph.remove_node(i)
            remove.append(i)

    for i in remove: worker.pop(i)

print("Total time: " + str(totalTime))

